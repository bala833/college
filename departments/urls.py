from django.urls import path
from . import views
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
# from django.conf.urls.defaults import *
from django.conf import settings

# app_name = 'departments'
urlpatterns = [
    # path('student/', views.student_list, name='student_list'),
    url(r'^department_list/$', views.department_list, name='department_list'),
    url(r'^create/$', views.add_department, name='add_department'),
    url(r'^(?P<pk>[\d-]+)/update/$', views.edit_department, name='edit_department'),
    url(r'^(?P<pk>[\d-]+)/delete/$', views.delete_department, name='delete_department'),
] 
