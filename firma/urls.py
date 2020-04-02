from django.conf.urls import url
from django.contrib import admin
from django.views.generic import ListView
from .models import Firm

from .views import (index, FirmListView)

from django.urls import path
from . import views


app_name = "firma"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:firm_name>/results/', views.results, name='results'),
    path('allfirm/', FirmListView.as_view(), name='allfirm'),

]


# from django.urls import path
# from . import views
#
# app_name = "firma"
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
# ]