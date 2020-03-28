from django.conf.urls import url
from django.contrib import admin
from .views import (index)

from django.urls import path
from . import views

app_name = "firma"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:firm_name>/results/', views.results, name='results'),
]


# from django.urls import path
# from . import views
#
# app_name = "firma"
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
# ]