from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class Attendee(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    post_nominal = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



'''
--- Subject
--- --- Topic
--- --- --- Course
--- --- --- 
'''

class Presenter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    post_nominal = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.post_nominal}"
    

class Subject(models.Model):
    SUBJECT_01 = 'SUB_01'
    SUBJECT_02 = 'SUB_02'
    SUBJECT_03 = 'SUB_03'
    SUBJECT_04 = 'SUB_04'
    SUBJECT_05 = 'SUB_05'

    SUBJECT_CHOICES =[
    (SUBJECT_01, 'Subject 1'),
    (SUBJECT_02, 'Subject 2'),
    (SUBJECT_03, 'Subject 3'),
    (SUBJECT_04, 'Subject 4'),
    (SUBJECT_05, 'Subject 5')
    ]

    subject = models.CharField(max_length= 20, choices=SUBJECT_CHOICES, blank=False)
    slug = models.SlugField()

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('course:subject-detail', kwargs={
            'slug': self.slug
    })



class Topic(models.Model):
    TOPIC_01 = 'TOP_01'
    TOPIC_02 = 'TOP_02'
    TOPIC_03 = 'TOP_03'
    TOPIC_04 = 'TOP_04'
    TOPIC_05 = 'TOP_05'
    
    TOPIC_CHOICES =[
    (TOPIC_01, 'Topic 1'),
    (TOPIC_02, 'Topic 2'),
    (TOPIC_03, 'Topic 3'),
    (TOPIC_04, 'Topic 4'),
    (TOPIC_05, 'Topic 5')
    ]


    topic = models.CharField(max_length= 20, choices=TOPIC_CHOICES, blank=False)
    slug = models.SlugField()

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse("course:topic_detail", kwargs={
            "slug": self.subject.slug,
            "topic": self.topic
    })
    

class Course(models.Model):
    name = models.CharField(max_length=200)
    atendees = models.ManyToManyField(Attendee)
    presenters = models.ManyToManyField(Presenter)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    slug = models.SlugField(default='slug name')
    description = models.TextField(max_length=500)
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    thumbnail = models.ImageField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=False)
    last_updated = models.DateTimeField(auto_now=True)
    duration = models.IntegerField(blank=False)
    broadcast_time = models.DateField()
    headshot = models.ImageField(blank=True)
    presentation_file = models.FileField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("course:course_list", kwargs={
            "subject_slug": self.subject.slug,
            "topic_slug": self.topic.slug,
            "course_slug": self.course.slug            
    })
    
    

class Comment(models.Model):
    user = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    post= models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class CourseView(models.Model):
    user = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    post= models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    post = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username