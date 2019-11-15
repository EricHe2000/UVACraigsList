
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from login.forms import EditProfileForm
from posts.models import Post



# def profile(request, pk=None):
#     if pk:
#         user = User.objects.get(pk=pk)
#     else:
#         user = request.user
#     args = {'user': user}
#     return render(request, 'login/profile.html', args)

def update_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'login/edit_profile.html', args)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
      
    
    args = {'user': user}
    return render(request, 'login/profile.html', args)

def index(request):

    context = {

        'user': User.objects.order_by('-date')
    if request.user.is_authenticated else []
    }

    return render(request, '', context)


def logout_view(request):
    logout(request)
    return redirect('/')  