"""Define patrones de URL para users."""
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Incluye las URLs de autenticación por default.
    path('', include('django.contrib.auth.urls')),
    # Página de registro.
    path('register/', views.register, name='register'),
]