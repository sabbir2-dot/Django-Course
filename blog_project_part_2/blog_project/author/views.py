from django.shortcuts import render, redirect
from .forms import RegistrationForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from posts.models import Post
# Create your views here.

# def add_author(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect("add_author")
#     else:
#         author_form = forms.AuthorForm()
#     return render(request, 'add_author.html', {'form': author_form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Created Successfully')
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form' : form, 'type': 'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username = name, password = userpass)
            if user is not None:
                login(request,user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form' : form, 'type': 'Login'})

@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data' : data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ChangeUserData(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ChangeUserData(instance = request.user)
    return render(request, 'update_profile.html', {'form' : form})

@login_required
def pass_Change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect(profile)
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request, 'pass_change.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user_login')