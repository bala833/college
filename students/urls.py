from django.urls import path
from . import views
from django.conf.urls import include, url

# app_name = 'students'
urlpatterns = [
    # path('student/', views.student_list, name='student_list'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^create/$', views.add_student, name='add_student'),
    url(r'^(?P<pk>[\d-]+)/update/$', views.edit_student, name='edit_student'),
    url(r'^(?P<pk>[\d-]+)/delete/$', views.delete_student, name='delete_student'),
    # path('<int:teacher_id>/detail/', views.teacher_detail, name='teacher_detail'),
    # path('add/', views.addTeacherView, name='add'),
    # path('del/<int:pk>/', views.deleteView, name='delete'),
    # url(r'^(?P<vendor_slug>[\w-]+)/pending_order_list/$', views.pending_order_list, {'template_name': 'dashboard/pending_order_list.html'}, 'pending_order_list'),
]
