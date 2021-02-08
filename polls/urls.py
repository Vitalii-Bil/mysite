from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('triangle/', views.triangle_view, name='triangle'),
    path('person/', views.person_create, name='person-create'),
    path('person/<int:pk>/', views.person_update, name='person-update'),
    path('reminder/', views.reminder_view, name='reminder'),
]
