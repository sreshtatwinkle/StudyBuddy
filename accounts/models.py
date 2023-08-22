from django.db import models
from django.contrib.auth.models import User

# Create your models here.
Subject_choices=[
    ('python','python'),
    ('java','java'),
    ('html,css.js','html,css,js'),
    ('React','React'),
    ('Computer Networks','Computer Networks'),
    ('Databases','Databases'),
    ('C++','C++'),
    ('None','None')
]



class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50,choices=Subject_choices)
    subject2 = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    def __str__(self):
        return self.username