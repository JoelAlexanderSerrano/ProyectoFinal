from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('create_page/', views.create_page, name='create_page'),
    path('edit_page/<int:pk>/', views.edit_page, name='edit_page'),
    path('delete_page/<int:pk>/', views.delete_page, name='delete_page'),
    path('profile/', views.get_profile, name='get_profile'),
]
