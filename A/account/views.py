import random

from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic
from django.contrib.auth import login, logout, authenticate
from utils import send_otp_code
from .forms import UserRegistrationForm, VerifyCodeForm, UserLoginForm
from .models import OtPCode, User
from django.views.generic.edit import CreateView
from django.views.generic import FormView


# class UserRegisterView(View):
#     form_class = UserRegistrationForm
#     template_name = 'acount/register.html'
#
#     def get(self, request):
#         form = self.form_class
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             random_code = random.randint(999, 10000)
#             send_otp_code(form.cleaned_data['phone'], random_code)
#             OtPCode.objects.create(phone=form.cleaned_data['phone'], code=random_code)
#             request.session['user_registration_info'] = {
#                 'phone': form.cleaned_data['phone'],
#                 'email': form.cleaned_data['email'],
#                 'full_name': form.cleaned_data['full_name'],
#                 'password': form.cleaned_data['password'],
#             }
#             messages.success(request, 'we sent you a code', 'success')
#             return redirect('account:verifyCode')
#         return render(request, self.template_name, {'form': form})

class UserRegisterView(FormView):
    template_name = 'acount/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('account:verifyCode')

    def form_valid(self, form):
        self._UserRegister(form.cleaned_data)
        messages.success(self.request, 'we sent you a code', 'success')
        return super().form_valid(form)

    def _UserRegister(self, data):
        random_code = random.randint(999, 10000)
        send_otp_code(data['phone'], random_code)
        OtPCode.objects.create(phone=data['phone'], code=random_code)
        self.request.session['user_registration_info'] = {
            'phone': data['phone'],
            'email': data['email'],
            'full_name': data['full_name'],
            'password': data['password'],
        }


class UserRegisterVerifyCodeView(View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'acount/verifycode.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtPCode.objects.get(phone=user_session['phone'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(email=user_session['email'], phone=user_session['phone'],
                                         full_name=user_session['full_name'], password=user_session['password'])
                code_instance.delete()
                messages.success(request, 'you registered sucessfully', 'success')

            else:
                messages.error(request, 'this cod is wrong', 'danger')
                return redirect('account:verifyCode')
            return redirect('home:home')


# class UserLoginView(View):
#     from_class = UserLoginForm
#
#     def get(self, request):
#         form = self.from_class
#         return render(request, 'acount/login.html', {'form': form})
#
#     def post(self, request):
#         form = self.from_class(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, phone=cd['phone'], password=cd['password'])
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'you can login sucessfully', 'success')
#                 return redirect('home:home')
#             messages.error(request, 'phone or password is wrong', 'danger')
#         return render(request, 'acount/login.html', {'form': form})

class UserLoginView(FormView):
    template_name = 'acount/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        cd = form.cleaned_data
        user = authenticate(self.request, phone=cd['phone'], password=cd['password'])
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'you can login sucessfully', 'success')
        else:
            messages.error(self.request, 'phone or password is wrong', 'danger')
        return super().form_valid(form)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'your logout sucessfully', 'success')
        return redirect('home:home')
