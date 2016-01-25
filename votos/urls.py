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
from django.contrib.auth import views as auth_views
from apps.votos.views import IndexView, ListarEstadoView, ListarAgendadoView, ListarFinalizadoView, MenuView, RegistrarCharlaView

urlpatterns = [
    url(r'^$', IndexView.as_view() ,name='index' ),
    url(r'^agendado$', ListarAgendadoView.as_view(), name='agendado' ),
    url(r'^finalizado$', ListarFinalizadoView.as_view() ,name='finalizado' ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^menu$', MenuView.as_view(), name='menu'),
    url(r'^registrar_charla$', RegistrarCharlaView.as_view(), name='registra_charla'),
    url(r'^posibles$', ListarEstadoView.as_view() ,name='posibles' ),# en realidad, se va a tener que cambiar el index, asi que de una vez apuntare a este en base
    url(r'^accounts/login/$', auth_views.login),
]