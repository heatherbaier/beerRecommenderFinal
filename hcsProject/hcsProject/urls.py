# import packages
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from chineseApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.HomePageView),
    url(r'^methodology/$', views.MethodologyView.as_view()),
]
