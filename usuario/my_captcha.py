from django import forms
from captcha.fields import ReCaptchaField
from farma_pet import settings

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField(public_key=settings.RECAPTCHA_PUBLIC_KEY, private_key=settings.RECAPTCHA_PRIVATE_KEY)