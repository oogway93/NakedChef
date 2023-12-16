from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import UpdateView

from .forms import UserCreationForm, UserProfileForm
from .models import User
from utils.views import TitleMixin
from users.tasks import send_contact_email_message_task


# @method_decorator(cache_page(timeout=60 * 30), name='dispatch')
class Register(TitleMixin, View):
    template_name = 'registration/register.html'
    title = 'Регистрация аккаунта'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Успешная регистрация!')
            send_contact_email_message_task.delay("Greetings!", self.request.user.id)
            return redirect('menu:main')
        context = {
            'form': form
        }
        messages.error(request, 'Провал в регистрации!')
        return render(request, self.template_name, context)


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Профиль: {self.request.user}'
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))
