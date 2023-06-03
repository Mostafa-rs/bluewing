from django import forms

from .models import *


class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد نمایید'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'ایمیل خود را وارد نمایید'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'نام خود را وارد نمایید'}))
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی خود را وارد نمایید'}))
    password_1 = forms.CharField(max_length=20,
                                 widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور خود را وارد نمایید'}))
    password_2 = forms.CharField(max_length=20,
                                 widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور خود را مجددا وارد نمایید'}))

    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('این نام کاربری قبلا ثبت شده است!')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل قبلا ثبت شده است!')
        return email

    def clean_password_2(self):
        password1 = self.cleaned_data['password_1']
        password2 = self.cleaned_data['password_2']
        if password1 != password2:
            raise forms.ValidationError('رمز عبور با هم مطابقت ندارند!')
        elif len(password2) < 8:
            raise forms.ValidationError('رمز عیور شما کوتاه است!')
        elif not any(x.isupper() for x in password2):
            raise forms.ValidationError('رمز عبور می بایست حداقل یک حرف بزرگ داشته باشد!')
        return password1


class UserLoginForm(forms.Form):
    user = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد نمایید'}))
    password = forms.CharField(max_length=20,
                               widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور خود را وارد نمایید'}))


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address']
