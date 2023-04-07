from django.views.generic import ListView
from django.shortcuts import render
from catalog.models import Product

from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy
from users.models import User
from users.forms import UserForm, UserCustomCreationForm
from django.views import View
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    model = User
    # form_class = UserCustomCreationForm
    # success_url = reverse_lazy('catalog:Product_list')
    template_name = 'users/login1.html'

class CustomRegisterView(CreateView):
    model = User
    form_class = UserForm
    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()

            # if form.data.get('need_generate', False):
            #     self.object.set_password(
            #         self.object.make_random_password(length=12)
            #     )
            #     self.object.save()
            self.object.is_active = False
            #send_register_mail()
            self.object.save()
        return super().form_valid(form)

    # if (form.is_valid()):
    #     cd = form.cleaned_data
    #     user = User.objects.create_user(cd["email"], cd["phone], cd["country"], cd["avatar"])
    #     user.first_name = cd["FirstName"]
    #     user.last_name = cd["LastName"]
    #     user.save()
    #     # Save userinfo record
    #     uinfo = user.get_profile()
    #     uinfo.middle_name = cd["MiddleName"]
    #     uinfo.save()


    #
    # success_url = reverse_lazy('catalog:Product_list')


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
    template_name = 'users/register.html'

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
class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('catalog.set_published_status'):
            return queryset

        return queryset.filter(published_status=True)
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

