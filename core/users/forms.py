from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from users.models import CustomUser
from django import forms


class UserCreateForm(UserCreationForm):

    forms.CharField(widget=forms.HiddenInput(), required=False)
    captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = ["email", "password1", "password2"]
        # widgets = {'email': forms.HiddenInput()}


