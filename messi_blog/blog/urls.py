from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import SignUpView, MyLoginView, MyLogoutView, HomeView, ProfileView, ProfileEditView, about_me, search

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('accounts/logout/', MyLogoutView.as_view(next_page='post_list'), name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('accounts/profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('about-me/', about_me, name='about_me'),
    path('search/', search, name='search'),
]
