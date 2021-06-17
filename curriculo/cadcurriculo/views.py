from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import LoginForm, UserRegistrationForm, \
                    UserEditForm, ProfileEditForm, UserDeleteForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


User = get_user_model()

@login_required
def dashboard(request):
    return render(request,
                  'cadcurriculo/dashboard.html',
                  {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                          'cadcurriculo/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                'cadcurriculo/register.html',
                {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Alteração efetuada com sucesso!')
        else:
            messages.error(request, 'Atenção. Não foi possível efetuar a alteração!')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'cadcurriculo/edit.html',
                  {'user_form': user_form,
                  'profile_form': profile_form})

@login_required
def delete(request, id):
    usuario = get_object_or_404(User, pk=id)
    usuario.delete()
    messages.error(request, 'Cadastro apagado. Para acessar novamente efetue um novo cadastro!')
    return redirect('logout')

def termo(request):
    return render(request,
                  'cadcurriculo/termos.html')