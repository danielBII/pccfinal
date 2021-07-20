from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import PostForm, FormLogin, FormRecovery, FormRedefine
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required



def create_accont(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST["username"], password=request.POST["password1"])
            login(request, user)
            return redirect('/')
        else:
            print('errors ->', form.errors)
            context = {
                'form': form
            }
            return render(request, 'accounts/form.html', context)
    else:
        form = PostForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/form.html', context)


@login_required
def account_profile(request):
    id_ = request.user.id
    profile = User.objects.get(pk=id_)
    print(profile.first_name)
    return render(request, 'accounts/profile.html', {'profile':profile})


@login_required
def account_profile_edit(request):

    user = get_object_or_404(User, pk=request.user.id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('errors ->', form.errors)
            context = {
                'form': form
            }
            return render(request, 'accounts/form.html', context)
    else:
        form = PostForm(instance=user)
        context = {
            'form': form
        }
        return render(request, 'accounts/form.html', context)        


def login_view(request):
    if request.method == "POST":
        formLogin = FormLogin(request.POST)
        if formLogin.is_valid():
            user = authenticate(request, username=formLogin['username'].value(), password=formLogin['password'].value())
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'accounts/login.html', {'form':formLogin})
        else:
            print(formLogin.errors)
            return render(request, 'accounts/login.html', {'form':formLogin})
    else:
        formLogin = FormLogin()
        return render(request, 'accounts/login.html', {'form':formLogin})

def logout_view(request):
    logout(request)
    return redirect('/')


def recovery_password(request):
    if request.method == "POST":
        form = FormRecovery(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            send_mail(
                subject='Recuperação de Senha',
                message='Você clicou em recuperar senha e aqui estamos.<br/> Clique no link e redefina: <a href="http://localhost:8000/account/click-password/'+email+'">Clique Aqui</a>',
                from_email=EMAIL_HOST_USER,
                fail_silently=False,
                recipient_list=[email]
            )
            return redirect('/')
        else:
            return render(request, 'accounts/recovery.html')
    else:
        form = FormRecovery()
        context = {
            'form': form
        }
        return render(request, 'accounts/recovery.html', context)


def redefine_view(request, email):
    if request.method == "POST":
        formRed = FormRedefine(request.POST)
        if formRed.is_valid():
            try:
                user = User.objects.get(email=email)
            except Exception as err:
                return render(request, 'accounts/redefine.html')

            if request.POST['password1'] == request.POST['password2'] :
                user.set_password(request.POST['password1'])
                user.save()
                return redirect('accounts:profile')
            else:
                return render(request, 'accounts/redefine.html', {'form':formRed})
        else:
            return render(request, 'accounts/redefine.html', {'form':formRed})
    else:
        formRed = FormRedefine()
        return render(request, 'accounts/redefine.html', {'form':formRed})