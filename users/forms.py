from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Product

User = get_user_model()

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Використовуємо кастомну модель
        fields = ('username', 'email', 'password1', 'password2')

class CustomRegisterForm(forms.ModelForm):
    username = forms.CharField(
        label="Nazwa użytkownika",
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        label="Hasło",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label="Potwierdź hasło",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Hasła się nie zgadzają.")
        return password2

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nazwa użytkownika",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label="Hasło",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
