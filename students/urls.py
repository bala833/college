from django.urls import path
from . import views


app_name = 'students'
urlpatterns = [
    path('student/', views.student_list, name='student_list'),
    # path('<int:teacher_id>/detail/', views.teacher_detail, name='teacher_detail'),
    # path('add/', views.addTeacherView, name='add'),
    # path('del/<int:pk>/', views.deleteView, name='delete'),
]