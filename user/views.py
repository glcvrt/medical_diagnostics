import random

from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from user.forms import UserRegisterForm, UserProfileForm
from user.models import User

from django.utils.translation import gettext_lazy as _


class UserLogout(LogoutView):
    http_method_names = ["post", "options"]
    template_name = "diagnostics/home_page.html"
    extra_context = None

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        logout(request)
        redirect_to = 'home_page'
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = 'home_page'
        context.update(
            {
                "site": 'home_page',
                "site_name": 'home_page',
                "title": _("Logged out"),
                "subtitle": None,
                **(self.extra_context or {}),
            }
        )
        return context


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:verify_email')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save()
            send_mail(
                subject='Подтверждение почты',
                message=f'Код {new_user.ver_code}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[new_user.email]
            )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('user:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('diagnostics:home_page'))


class VerificationTemplateView(TemplateView):
    template_name = 'user/msg_email.html'

    def post(self, request):
        ver_code = request.POST.get('ver_code')
        user_code = User.objects.filter(ver_code=ver_code).first()

        if user_code is not None and user_code.ver_code == ver_code:
            user_code.is_active = True
            user_code.save()
            return redirect('user:login')
        else:
            return redirect('user:verify_email_error')


class ErrorVerificationTemplateView(TemplateView):
    template_name = 'user/verify_email_error.html'
    success_url = reverse_lazy('user:msg_email')
