import random

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from utils import send_top_code
from .forms import UserRegistrationForm
from .models import OtPCode


class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'acount/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(999, 10000)
            send_top_code(form.cleaned_data['phone'], random_code)
            OtPCode.objects.create(phone=form.cleaned_data['phone'], code=form.cleaned_data['code'])
            request.session['user_registration_info'] = {
                'phone': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'fulll_name': form.cleaned_data['fulll_name'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'we sent you a code', 'sucess')
            return redirect('account:verifyCode')
        return render(request, self.template_name, {'form': form})


class UserRegisterVerifyCodeView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
