import random

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from utils import send_otp_code
from .forms import UserRegistrationForm, VerifyCodeForm
from .models import OtPCode, User


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
            send_otp_code(form.cleaned_data['phone'], random_code)
            OtPCode.objects.create(phone=form.cleaned_data['phone'], code=random_code)
            request.session['user_registration_info'] = {
                'phone': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'we sent you a code', 'sucess')
            return redirect('account:verifyCode')
        return render(request, self.template_name, {'form': form})


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
                messages.success(request, 'you registered sucessfully', 'sucess')

            else:
                messages.error(request, 'this cod is wrong', 'danger')
                return redirect('account:verifyCode')
            return redirect('home:home')
