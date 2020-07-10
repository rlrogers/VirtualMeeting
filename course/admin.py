from django.contrib import admin
from .models import Course, Comment, CourseView, Like, User

admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(CourseView)
admin.site.register(Like)
admin.site.register(User)
