from django.contrib import admin
from .models import Course, Comment, CourseView, Like, Attendee

admin.site.register([
                    Course,
                    Comment,
                    CourseView,
                    Like,
                    Attendee
                ])
