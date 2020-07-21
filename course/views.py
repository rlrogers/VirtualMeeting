from django.shortcuts import render
from django.views.generic import (ListView,
                                 DetailView,
                                 UpdateView,
                                 CreateView,
                                 DeleteView)
from .models import Attendee, Presenter, Subject, Topic, Course, Comment, CourseView, Like
from .forms import CourseForm



class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course
    

class CourseCreateView(CreateView):
    form_class = CourseForm
    model = Course
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context
    
class CourseUpdateView(UpdateView):
    form_class = CourseForm
    model = Course
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        }) 
        return context
    


class CourseDeleteView(DeleteView):
    model = Course
    success_url = '/'


class SubjectListView(ListView):
    model = Subject


class SubjectDetailView(DetailView):
    model = Subject


class TopicListView(ListView):
    model = Topic


class TopicDetailView(DetailView):
    model = Topic