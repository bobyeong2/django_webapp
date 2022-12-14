from django.urls import path
from django.views.generic import TemplateView

from projectapp.views import ProjectCreateView,ProjectDetailView,ProjectListView, ProjecteDeleteView

app_name = 'projectapp'
urlpatterns = [
    path('create/',ProjectCreateView.as_view(),name='create'),
    path('detail/<int:pk>',ProjectDetailView.as_view(),name='detail'),
    path('list/',ProjectListView.as_view(),name='list'),
    path('delete/<int:pk>',ProjecteDeleteView.as_view(),name = 'delete')
]