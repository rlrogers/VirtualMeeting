from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Course(models.Model):
    SURGICAL = 'SRG'
    MEDICAL = 'MDCL'
    MULTIDISCIPLINARY = 'MLTDSY'
    INDUSTRY = 'INSTY'
    RESIDENT_FELLOW = 'RFW'

    DISIPLINE_CHOICES =[
    (SURGICAL, 'Surgical'),
    (MEDICAL, 'Medical'),
    (MULTIDISCIPLINARY, 'Multidisciplinary'),
    (INDUSTRY, 'Industry'),
    (RESIDENT_FELLOW, 'Resident & Fellow')
    ]

    title = models.CharField( max_length=100, blank=False)
    slug = models.SlugField(default='slug name')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=500)
    discipline = models.CharField(max_length= 20, choices=DISIPLINE_CHOICES, default=MEDICAL)
    thumbnail = models.ImageField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=False)
    last_updated = models.DateTimeField(auto_now=True)
    duration = models.IntegerField(blank=False)
    broadcast_time = models.DateField()
    live = models.BooleanField(default=False)
    headshot = models.ImageField(blank=True)
    presentation_file = models.FileField()

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class CourseView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username