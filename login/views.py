
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User


def profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'login/profile.html', args)