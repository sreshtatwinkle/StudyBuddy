from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
MODULE_OPTIONS = [
    ("PY", "Python"),
    ("JAVA", "Java"),
    ("HTML,CSS,JS", "Html,css,js"),
    ("REACT", "REACT"),
    ("CN", "Comupter Networks"),
    ('DB','Databases'),
    ('C++','C++'),
    ('None','None')
]
class User_Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,blank=True)
    module = models.CharField(max_length=50,choices=MODULE_OPTIONS)
    module2 = models.CharField(max_length=50,blank=True)
    profile_pic = models.ImageField(default='default-avatar.png', upload_to='users/', null=True, blank=True)

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        User_Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.user_profile.save()