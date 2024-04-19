from django.conf import settings
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetDoneView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView

from user.forms import UserRegisterForm, UserProfileForm
from user.models import User

from django.utils.translation import gettext_lazy as _


def users(request):
    user = User.objects.all()
    return render(request, 'user/user.html', {'user': user})


class UserLogin(LoginView):
    template_name = 'user/login.html'
    success_url = reverse_lazy('diagnostics:home_page')


class UserLogout(LogoutView):
    http_method_names = ["post", "options"]
    template_name = "diagnostics/home_page.html"
    extra_context = None

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        logout(request)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.save()

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_url = reverse_lazy('user:confirm_email', kwargs={'uidb64': uid, 'token': token})

        current_site = '127.0.0.1:8000'

        send_mail(
            subject='Регистрация на платформе',
            message=f"Завершите регистрацию, перейдя по ссылке: http://{current_site}{activation_url}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return redirect('user:email_confirmation_sent')


class UserConfirmEmailView(View):

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('user:email_confirmed')
        else:
            return redirect('user:email_confirmation_failed')


class UserConfirmedView(TemplateView):
    """ Выводит информацию об успешной регистрации пользователя """
    template_name = 'user/registration_confirmed.html'


class UserConfirmationFailView(View):
    """ Выводит информацию о невозможности зарегистрировать пользователя """
    template_name = 'user/email_confirmation_failed.html'


class UserConfirmationSentView(PasswordResetDoneView):
    """ Выводит информацию об отправке на почту подтверждения регистрации """
    template_name = "user/registration_sent_done.html"


def generate_new_password(request):
    """ Генерирует новый пароль пользователя """
    new_password = get_random_string(length=9)

    send_mail(
        subject='Новый пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )

    request.user.set_password(new_password)
    request.user.save()

    return redirect(reverse('catalog:home'))


def regenerate_password(request):
    """ Генерирует новый пароль пользователя """
    if request.method == 'POST':
        email = request.POST.get('email')
        # Получаем пользователя по email
        user = User.objects.get(email=email)

        # Генерируем новый пароль
        new_password = get_random_string(length=9)

        # Изменяем пароль пользователя
        user.set_password(new_password)
        user.save()

        # Отправляем письмо с новым паролем
        send_mail(
            subject='Восстановление пароля',
            message=f'Ваш новый пароль: {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )

        return redirect(reverse('catalog:home'))
    return render(request, 'user/regenerate_password.html')


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('user:profile')
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return self.request.user


class UserDetailView(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        context = {
            'object': user,
        }
        return render(request, 'user/profile.html', context)
