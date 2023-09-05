from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat_userprofile(models.Model):
    user_chat = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user_chat.username


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    is_seen =models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return f"{self.sender} to {self.receiver}: {self.content}"