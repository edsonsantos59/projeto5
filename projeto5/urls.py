from django.contrib import admin
from django.urls import path
from projeto5_website import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('admin/', admin.site.urls),
    path('pergunta_form/', views.pergunta_form, name='pergunta_form'),
    path('login/', views.login_user, name='login'),
    path('obrigado/', views.obrigado, name="obrigado"),
    path('test/', views.test, name="test"),
    path('logout/', views.logout_user, name='logout'),
    path('index/', views.index, name='index'),
    path('resultado/', views.resultado, name='resultado')
]