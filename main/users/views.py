from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import UserCreationForm


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'Успешная регистрация!')
            return redirect('main')
        context = {
            'form': form
        }
        messages.error(request, 'Провал в регистрации!')
        return render(request, self.template_name, context)


def profile(request):
    return render(request, 'registration/profile.html')
