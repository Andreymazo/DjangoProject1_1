from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from users.models import User
from users.forms import UserForm

class CustomLoginView(LoginView):
    template_name = 'CustomUser/login.html'
class UserCustomProfileView(UpdateView):
    model = User
    template_name = 'CustomUser/profile.html'
    form_class = UserForm
    success_url = reverse_lazy('users:home')

from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.views import View

from users.forms import UserCreationForm, UserForm


class Register(View):
    template_name = 'registration/register.html'
    def get(self, request):
        context = {
            'form': UserCreationForm()

        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request,self.template_name, context)

