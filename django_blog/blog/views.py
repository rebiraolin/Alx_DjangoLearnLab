from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    form = UserRegistrationForm()

    context = {'form': form}

    if request.method == 'GET':
        return render(request, 'blog/register.html', context)

    elif request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'GET':
        form = UserUpdateForm(instance=request.user)
        context = {'form': form}
        return render(request, 'blog/profile.html', context)
    elif request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
        else:
            return render(request, 'blog/profile.html', {'form': form})

def home(request):
    return render(request, 'blog/home.html')



