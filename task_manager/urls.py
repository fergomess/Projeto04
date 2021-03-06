"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from task.views import *  #importa as funções que estão na views do app task

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home),
    url(r'^sobre/', sobre),
    url(r'^tarefa/([0-9]{4})/', tarefa),
    url(r'^tarefaN/(?P<ano>[0-9]{4})/(?P<mes>[0-9]{2})', tarefaN),
    url(r'^tarefaN/(?P<dia>[0-9]{4})/(?P<mes>[0-9]{2})/(?P<ano>[0-9]{4})', tarefaD),
]
