from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm
import bcrypt
def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            """username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user = authenticate(username=username, password=hashed_password, first_name=first_name, last_name = last_name)
            login(request, user)"""
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})