from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user.apps import UserConfig
from user.views import RegisterView, ProfileView, VerificationTemplateView, generate_new_password, \
    ErrorVerificationTemplateView, UserLogout

app_name = UserConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('logout/', UserLogout.as_view(next_page='diagnostics:home_page'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verify_email/', VerificationTemplateView.as_view(), name='verify_email'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
    path('verify_email/error/', ErrorVerificationTemplateView.as_view(), name='verify_email_error'),
]
