from django.urls import path
from django.contrib import admin
from . import views
from . import views_auth
from django.conf.urls.static import static

urlpatterns = [
    path('', views_auth.index, name='index'),
    path('register/', views_auth.registration, name='register'),
    path('login/', views_auth.login_view, name='login'),
    path('logout/', views_auth.logout_view, name='logout'),
    path('account/', views_auth.account, name='account'),
    path('create/', views.create_view, name='create'),
    path('edit/<int:transaction_id>', views.edit_view, name='edit'),
    path('about', views.about, name='about'),
]
