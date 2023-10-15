from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'username', 
                   'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'}), 
        )
    email = forms.CharField(
        label='',
        required=True,
        widget=forms.EmailInput(
            attrs={'placeholder': 'email', 
                   'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'}), 
        )
    
    password1 = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'password', 
                   'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'}), 
        )
    
    password2 = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'confirm password', 
                   'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'}), 
        )

    class Meta:
        model = User  # Replace 'User' with your custom User model if you have one
        fields = ('username', 'email', 'password1', 'password2')


class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': 'username', 
                   'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'}), 
        )
    password = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'password', 
                   'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'}), 
        )
    

    class Meta:
        model = User  # Replace 'User' with your custom User model if you have one
        fields = ('username', 'email', 'password1',)
