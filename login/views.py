
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout


# def profile(request, pk=None):
#     if pk:
#         user = User.objects.get(pk=pk)
#     else:
#         user = request.user
#     args = {'user': user}
#     return render(request, 'login/profile.html', args)


def index(request):
	context = {
		'user': User.objects.order_by('-date')
	if request.user.is_authenticated else []
	}

	return render(request, 'login/profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')  