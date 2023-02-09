from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy
from users.models import User
from users.forms import UserForm
from django.views import View
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

class UserEditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserChangeForm###Chto u Olega v form.py????? Eto krasota prosto
    #form_class = UserForm
    success_url = reverse_lazy('catalog:catalog')

    def get_object(self, queryset=None):
        return self.request.user
class CustomRegisterView(CreateView):
    model = User
    form_class = UserCreationForm

    # def form_valid(self, form):
    #     if form.is_valid():
    #         self.object = form.save()
    #         # if form.data.get('need_generate', False):
    #         #     self.object.set_password(
    #         #         self.object.make_random_password(length=12)
    #         #     )
    #         #     self.object.save()
    #         self.object.is_active = False
    #         send_register_mail()
    #         self.object.save()
    #     return super().form_valid(form)
class EmailVerify(View):
    pass

from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.views import View

from users.forms import UserCustomCreationForm, UserForm


# class Register(View):
#     template_name = 'registration/register.html'
#     def get(self, request):
#         context = {
#             'form': UserCustomCreationForm()
#
#         }
#         return render(request, self.template_name, context)
#     def post(self, request):
#         form = UserCustomCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # username = form.cleaned_data.get('username')
#
#             password = form.cleaned_data.get('password1')
#             # user = authenticate(username=username, password=password)
#             # login(request, user)
#             return redirect('home')
#         context = {
#             'form': form
#         }
#         return render(request, self.template_name, context)

