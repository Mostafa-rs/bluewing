from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from .forms import *
from .models import *


# Create your views here.


def user_register(request):
    # if request.method == 'POST':
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     user = request.POST['user_name']
    #     email = request.POST['email']
    #     password = request.POST['password_1']
    #     confirm_password = request.POST['password_2']
    #
    #     if password == confirm_password:
    #         if User.objects.filter(email=email).exists():
    #             messages.error(request, 'این ایمیل قبلا ثبت شده است!', 'danger')
    #             return redirect('accounts:user_register')
    #         elif User.objects.filter(username=user).exists():
    #             messages.error(request, 'این نام کاربری قبلا ثبت شده است!', 'danger')
    #             return redirect('accounts:user_register')
    #         else:
    #             User.objects.get_or_create(username=user,
    #                                        first_name=first_name, last_name=last_name, email=email,
    #                                        password=password)
    #
    #         return redirect('accounts:login')
    #     else:
    #         messages.error(request, 'رمز عبور با هم مطایقت ندارند!', 'danger')
    #         return redirect('accounts:user_register')
    #
    # else:
    #     return render(request, 'auth/register.html')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(username=data['user_name'], email=data['email'],
                                       first_name=data['first_name'],
                                       last_name=data['last_name'], password=data['password_2'])

            messages.success(request, 'registered', 'success')
            user.save()
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()

    context = {'form': form}

    return render(request, 'auth/register.html', context)


def user_login(request):
    # if request.method == "POST":
    #     password = request.POST['password']
    #     user = auth.authenticate(request, password=password)
    #
    #     if user is not None:
    #         auth.login(request, user)
    #         messages.success(request, 'ورود با موفقیت انجام شد.', 'success')
    #         return redirect('home:home')
    #     else:
    #         messages.error(request, 'نام کاربری یا رمز عبور اشتباه است!', 'danger')
    #
    # return render(request, "auth/login.html")
    request.session['s_key'] = request.session.session_key
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['user'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'ورود با موفقیت انجام شد.', 'success')
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                del request.session['s_key']
                return redirect('home:home')
            else:
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است!', 'danger')
    else:
        form = UserLoginForm()

    return render(request, 'auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'خروج با موفقیت انجام شد.', 'warning')
    return redirect('home:home')


@login_required(login_url='accounts:login')
def user_profile(request):
    profile = Profile.objects.get(user_id=request.user.id)
    return render(request, 'auth/profile.html', {'profile': profile})


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'با موفقیت ذخیره شد!', 'success')
            return redirect('accounts:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'auth/user_update.html', {'user_form': user_form, 'profile_form': profile_form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'رمز عبور جدید با موفقیت ذخیره شد!', 'success')
            return redirect('accounts:profile')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'auth/change.html', {'form': form})
