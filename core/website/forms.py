from django import forms
from .models import Contact, NewsLetter
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = ["sender","email", "name", "subject", "message"]


class NewsLetterForm(forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields = ["email", "sender"]
