"""votos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from apps.votos.views import  IndexView, ListarEstadoView, ListarAgendadoView, ListarFinalizadoView, MenuView, RegistrarCharlaView

urlpatterns = [
    url(r'^$', IndexView.as_view() ,name='index' )
    ,url(r'^menu$', MenuView.as_view(), name='menu' ),
    url(r'^charlas/posibles$', ListarAgendadoView.as_view(), name='charlas/posibles' ),
    url(r'^charlas/agendadas$', ListarAgendadoView.as_view(), name='charlas/agendadas' ),
    url(r'^charlas/finalizadas$', ListarFinalizadoView.as_view() ,name='charlas/finalizadas' ),
    url(r'^charlas/postular$', RegistrarCharlaView.as_view(), name='charlas/postular' ),
    url(r'^admin/', include(admin.site.urls)),
]
