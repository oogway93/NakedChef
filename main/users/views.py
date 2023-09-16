from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import UpdateView

from .forms import UserCreationForm, UserProfileForm
from .models import User
from menu.models import Basket


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


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basket'] = Basket.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))
