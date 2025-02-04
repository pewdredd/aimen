from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, message=f'Поздравляем! Вы успешно создали аккаунт - {username}')
            return redirect('aibots:home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html', {'form': form})





