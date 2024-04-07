from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Avatar, User
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm, ProfileEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not isinstance(self.request.user, AnonymousUser):
            try:
                avatar = self.request.user.avatar
            except Avatar.DoesNotExist:
                avatar = None
            context['avatar'] = avatar
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('post_list')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

class SignUpView(CreateView):
    template_name = 'blog/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Guardar el usuario
        response = super().form_valid(form)
        # Asignar avatar predeterminado
        default_avatar = Avatar.objects.get(name='default_avatar')
        self.object.avatar = default_avatar
        self.object.save()
        # Mensaje de éxito
        messages.success(self.request, '¡Te has registrado exitosamente!')
        return response

class MyLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm

class MyLogoutView(LogoutView):
    next_page = reverse_lazy('post_list')

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/home.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirige al usuario a la página de inicio de sesión si no está autenticado
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Verificar si el usuario tiene un avatar
        if hasattr(self.request.user, 'avatar'):
            context['avatar'] = self.request.user.avatar
        else:
            context['avatar'] = None
        return context

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener el usuario actual y pasarlo al contexto
        user = self.request.user
        context['user_data'] = user
        try:
            avatar = user.avatar
        except Avatar.DoesNotExist:
            avatar = None
        context['avatar'] = avatar
        return context

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileEditForm
    template_name = 'blog/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        # Obtener el usuario actual
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            avatar = self.request.user.avatar
        except Avatar.DoesNotExist:
            avatar = None
        context['avatar'] = avatar
        return context

def about_me(request):
    # Contenido sobre ti
    about_me_content = """
    Bievenidos, mi nombre es Joel Serrano, tengo 34 años, estoy realizando el curso
    de Python en Coder House, para poder conseguir un trabajo de Developer en una empresa.
    """

    return render(request, 'blog/about_me.html', {'about_me_content': about_me_content})

def search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(title__icontains=query)
    return render(request, 'blog/search_results.html', {'results': results})    