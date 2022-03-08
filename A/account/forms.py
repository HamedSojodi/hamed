from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from account.models import Profile


class UserRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-3-border border-dark '
                                                                      'shadow-lg p-2 mb-5 bg-white rounded',
                                                             'placeholder': 'User name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control mb-3 mt-3-border border-dark '
                                                                     'shadow-lg p-2 mb-5 bg-white rounded',
                                                            'placeholder': 'Email'}))
    password1 = forms.CharField(label='password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control mb-3 mt-3-border border-dark '
                                                                           'shadow-lg p-2 mb-5 bg-white rounded',
                                                                  'placeholder': 'Password'}))
    password2 = forms.CharField(label='confrim password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control mb-3 mt-3-border border-dark '
                                                                           'shadow-lg p-2 mb-5 bg-white rounded',
                                                                  'placeholder': 'Confrim Password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This Email alredy exists')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('This user name alredy exists')
        return username

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')
        if p1 and p2 and p2 != p1:
            raise ValidationError('password must match!!!')


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-3-border border-dark '
                                                                      'shadow-lg p-2 mb-5 bg-white rounded',
                                                             'placeholder': 'User name or Email'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3 mt-3-border border-dark '
                                                                          'shadow-lg p-2 mb-5 bg-white rounded',
                                                                 'placeholder': 'password'}))


class EditUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ('age', 'bio', 'image')
