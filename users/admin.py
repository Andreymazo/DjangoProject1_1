from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
#
from users.models import User

admin.site.register(User)
# # User = get_user_model()
# @admin.register(User)
# class UserAdmin(UserAdmin):
#     pass
#     # add_fieldsets = (
#     #     (
#     #         None,
#     #         {
#     #             "classes": ("wide",),
#     #             "fields": ( "email",  "password1", "password2")#,"avatar","country", 'phone',
#     #         },
#     #     ),
#     # )
#     # fieldsets = (
#     #     (None, {"fields": ("username", "password")}),
#     #     (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
#     #     (
#     #         _("Permissions"),
#     #         {
#     #             "fields": (
#     #                 "is_active",
#     #                 "is_staff",
#     #                 "is_superuser",
#     #                 "groups",
#     #                 "user_permissions",
#     #             ),
#     #         },
#     #     ),
#     #     (_("Important dates"), {"fields": ("last_login", "date_joined")}),
#     # )
# class UserCreationForm(UserCreationForm):
#
#     class Mets(UserCreationForm.Meta):
#         model = User

