from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )
    username = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.TextInput()
    )
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')
        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cleaned_data

    def save(self):
        data = self.cleaned_data
        print(data )
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        print(user)
        profile = Profile(user=user)
        print(profile)
        profile.save()