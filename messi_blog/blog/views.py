from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import ProfileForm
from .forms import PageForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Page
from .models import Profile

@login_required
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def user_login(request): #Logueo de usuario
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Iniciar sesión
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def user_logout(request): #Deslogueo de usuario
    logout(request)
    return redirect('login')

def register(request): #Registro de usuario
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

def about(request): #About
    return render(request, 'blog/about.html')

@login_required
def edit_profile(request): #Editar perfil
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al usuario a la página de inicio después de editar el perfil
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'blog/edit_profile.html', {'form': form})

def contact(request): #Contacto
    return render(request, 'blog/contact.html')

def faq(request): #Preguntas frecuentes
    return render(request, 'blog/faq.html')


def create_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # O redirige a donde desees después de crear la página
    else:
        form = PageForm()
    return render(request, 'blog/create_page.html', {'form': form})

def edit_page(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return redirect('home')  # O redirige a donde desees después de actualizar la página
    else:
        form = PageForm(instance=page)
    return render(request, 'blog/edit_page.html', {'form': form})

def delete_page(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == 'POST':
        page.delete()
        return redirect('home')
    return render(request, 'blog/delete_page.html', {'page': page})

@login_required
def get_profile(request):
    # Obtener el perfil del usuario actualmente autenticado
    profile = Profile.objects.get(user=request.user)
    return render(request, 'blog/profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('get_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'blog/edit_profile.html', {'form': form})