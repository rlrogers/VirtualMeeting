from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from course.views import (
        CourseListView,
        CourseDetailView,
        CourseCreateView,
        CourseUpdateView,
        CourseDeleteView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',CourseListView.as_view(), name='list'),
    path('create/',CourseCreateView.as_view(), name='create'),
    path('<slug>/',CourseDetailView.as_view(), name='detail'),
    path('<slug>/update',CourseUpdateView.as_view(), name='update'),
    path('<slug>/delete',CourseDeleteView.as_view(), name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   