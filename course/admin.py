from django.contrib import admin
from .models import Presenter, Subject, Topic, Course, Comment, CourseView, Like, Attendee

admin.site.register([
                    Presenter,
                    Subject,
                    Topic,
                    Course,
                    Comment,
                    CourseView,
                    Like,
                    Attendee
                ])
