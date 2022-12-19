from django.urls import path

from . import views

urlpatterns = [
    path('add-acao/', views.add_acao, name='add acao'),
    path('get-acao/', views.get_acao, name='get acao'),
    path('login-user/', views.login_user, name='login user'),
]