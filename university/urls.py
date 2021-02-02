from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'university'
urlpatterns = [
    path('student', cache_page(10)(views.StudentList.as_view()), name='student_list'),
    path('student/<int:pk>/', cache_page(10)(views.StudentDetail.as_view()), name='student_detail'),
    path('student/create/', views.StudentCreate.as_view(), name='student_create'),
    path('student/update/<int:pk>', views.StudentUpdate.as_view(), name='student_update'),
    path('student/delete/<int:pk>', views.StudentDelete.as_view(), name='student_delete'),
    path('', cache_page(10)(views.UniversityList.as_view()), name='university_list'),
]
