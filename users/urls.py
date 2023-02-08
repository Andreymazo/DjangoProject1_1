from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView
from users.apps import UsersConfig
from users.views import Register

# from users.views import CustomLoginView, UserCustomProfileView #EmailVerify

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('confirm_email/', TemplateView.as_view(template_name='confirm_email.html'), name='confirm_email'),
    # path(
    #     'verify_email/<uid64>/<token>/',
    #     EmailVerify.as_view(),
    #     name='verify_email',
    #      ),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    #path('profile/', UserCustomProfileView.as_view(), name='profile'),
    # path('profile/verified-email-field/', UserCustomProfileView.as_view(), name='verified_email_field.urls'),
]