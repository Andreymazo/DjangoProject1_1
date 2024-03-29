from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager
from django.apps import apps
from django.contrib.auth.hashers import make_password
from users.models import User
from django.contrib.auth.forms import UserChangeForm
# from forms_mixins import StyleFormMixin
from users.models import User

###############################################
# from catalog.form_mixins import StyleFormMixin
# class CustomEditUserForm(StyleFormMixin, UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('email', 'avatar', "phone", "country",)
######################################################
UserCustom = get_user_model()


# class CustomUserManager(UserManager):
#     use_in_migrations = True
#
#     def _create_user(self, email, password, **extra_fields):
#         """
#         Create and save a user with the given username, email, and password.
#         """
#         if not email:
#             raise ValueError("The given email must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#
#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")
#
#         return self._create_user(email, password, **extra_fields)


class UserCustomCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    class Meta(UserCreationForm.Meta):
        model = UserCustom
        fields = ["email", "phone", "country", "avatar"]  #


# class CustomEditUserForm(StyleFormMixin, UserChangeForm):
#     class Meta:
#         model = User
#         fields = ['email', 'country', 'avatar', 'phone']
class UserForm(UserChangeForm):#StyleFormMixin,
    class Meta:
        model = User
        fields = ['email', 'country', 'avatar', 'phone']  #
        # field_classes = {"email": "email", "country": "country", "avatar": "avatar", "phone": "phone"}
