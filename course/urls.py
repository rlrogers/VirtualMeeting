from django.urls import path

from course.views import (
        CourseListView,
        CourseDetailView,
        CourseCreateView,
        CourseUpdateView,
        CourseDeleteView
)

app_name = 'course'

urlpatterns = [
    path('',CourseListView.as_view(), name='list'),
    path('create/',CourseCreateView.as_view(), name='create'),
    path('<slug>/',CourseDetailView.as_view(), name='detail'),
    path('<slug>/update',CourseUpdateView.as_view(), name='update'),
    path('<slug>/delete',CourseDeleteView.as_view(), name='delete'),
]
