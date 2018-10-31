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
from django.contrib.auth.views import logout

from apps.votos.views import (
    ListarEstadoView, ListarAgendadoView, ListarFinalizadoView,
    RegistrarCharlaView, DetalleCharlaView, ListarFaqView
)
from apps.votos.views import VotoView, login

urlpatterns = [
    url(r'^$', ListarEstadoView.as_view(), name='index'),
    url(r'^agendado$', ListarAgendadoView.as_view(), name='agendado'),
    url(r'^finalizado$', ListarFinalizadoView.as_view(), name='finalizado'),
    url(r'^faq$', ListarFaqView.as_view(), name='faq'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registrar_charla$',
        RegistrarCharlaView.as_view(),
        name='registrar_charla'),
    url(r'^votar/(?P<charla>\d+)$', VotoView.as_view(), name='votar'),
    url(r'^posible-charla/(?P<pk>\d+)$',
        DetalleCharlaView.as_view(),
        name='detalle_charla'),

    # Python Social Auth URLs
    # url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    url(r'^login', login, name="login"),
    url(r'^users/logout/$', logout,
        {'next_page': '/'},
        name="user-logout"),

]
