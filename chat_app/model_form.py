from django import forms
from .models import Message

class Message_Form(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'pdf_file']
