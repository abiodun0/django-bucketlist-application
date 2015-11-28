from django import forms
from django.forms import ModelForm, Textarea, TextInput, RadioSelect, PasswordInput, EmailInput
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    """This handles the model login form"""

    username = forms.CharField(label='Username', max_length=100,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Enter unique username',
                                   'autocomplete': 'off',
                                   'class': 'form-control'
                               }))
    password = forms.CharField(label='Password', max_length=100,
                               widget=forms.PasswordInput(attrs={
                                   'placeholder': 'Enter secret password',
                                   'class': 'form-control'
                               }))

    remember_me = forms.BooleanField(
        label='Remember Me', required=False)


class RegisterForm(ModelForm):

    """This handles the user registeration form """

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        widgets = {'username': TextInput(attrs={
            'placeholder': 'Your unique username',
            'autocomplete': 'off',
            'class': 'form-control'
        }),
            'password': PasswordInput(attrs={
                'placeholder': 'Create secret Password',
                'autocomplete': 'off',
                'class': 'form-control'}),

            'first_name': TextInput(attrs={
                'placeholder': 'Your Name',
                'autocomplete': 'off',
                'class': 'form-control'
            }),
            'last_name': TextInput(attrs={
                'placeholder': 'Last Name',
                'autocomplete': 'off',
                'class': 'form-control'}),
            'email': TextInput(attrs={
                'placeholder': 'Last Name',
                'autocomplete': 'off',
                'class': 'form-control'
            }),
        }

    password_conf = forms.CharField(max_length=100,
                                    widget=forms.PasswordInput(attrs={
                                        'placeholder': 'Verify secret password',
                                        'class': 'form-control',
                                    }))

    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(
            "This user already exist, please choose another username")

    def clean_email(self):
        try:
            User.objects.get(email=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(
            "This email already exist in the database, please use another email address")

    def clean(self):
        if 'password' in self.cleaned_data and 'password_conf' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_conf']:
                raise forms.ValidationError(
                    "You must type in the same password each time")
        return self.cleaned_data

    def save(self):
        new_user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )
        return new_user


class ProfileForm(RegisterForm):

    def __init__(self, *args, **kwargs):

        super(ProfileForm, self).__init__(*args, **kwargs)
        # the color field set to false
        self.fields['password'].required = False
        self.fields['password_conf'].required = False

    def clean_username(self):
        return self.cleaned_data['username']

    def clean_email(self):
        return self.cleaned_data['email']

    def save(self, commit=True):
        """overriden save method of the form class"""
        user = User.objects.get(username=self.cleaned_data['username'])
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
