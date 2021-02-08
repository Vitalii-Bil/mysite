from django.urls import path

from . import views

app_name = 'university'
urlpatterns = [
    path('student', views.StudentList.as_view(), name='student_list'),
    path('student/<int:pk>/', views.StudentDetail.as_view(), name='student_detail'),
    path('student/create/', views.StudentCreate.as_view(), name='student_create'),
    path('student/update/<int:pk>', views.StudentUpdate.as_view(), name='student_update'),
    path('student/delete/<int:pk>', views.StudentDelete.as_view(), name='student_delete'),
    path('', views.UniversityList.as_view(), name='university_list'),
]
