from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.views.generic import TemplateView
from users.apps import UsersConfig
from users.views import EmailVerify, CustomRegisterView, CustomLoginView, \
    UserEditProfileView
#Register,
# from users.views import CustomLoginView, UserCustomProfileView #EmailVerify

app_name = UsersConfig.name

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('', CustomLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('profile/', UserEditProfileView.as_view(), name='profile'),
    # path('confirm_email/', TemplateView.as_view(template_name='confirm_email.html'), name='confirm_email'),

    # path('users/password_reset', TemplateView.as_view(template_name='registration/password_reset_form.html'),
    #      name='password_reset'),
    # path(
    #     'verify_email/<uid64>/<token>/',
    #     EmailVerify.as_view(),
    #     name='verify_email',
    #      ),

    # path('register/', Register.as_view(), name='register')
    path('register/', CustomRegisterView.as_view(), name='register'),

    # path('profile/verified-email-field/', UserCustomProfileView.as_view(), name='verified_email_field.urls'),
]