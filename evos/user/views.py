from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('redir')
    if request.method == 'POST':
        forms = UserForm(request.POST)
        if forms.is_valid():
            user = forms.save()
            login(request, user)
            return redirect('redir')

    form = UserForm
    ctx = {'forms': form}
    return render(request, 'user/index.html', ctx)


def signIn(request):
    if request.user.is_authenticated:
        return redirect('redir')

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                print(f"Welcome {username}!")
                login(request, user)
                return redirect('redir')
            else:
                print("username or password error")
    form = ProfileForm()
    ctx = {'form': form}
    return render(request, 'user/signIn.html', ctx)


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    ctx = {
        'user': request.user,
    }
    return render(request, 'user/profile.html', ctx)


def logout_view(request):
    logout(request)
    return redirect('login')