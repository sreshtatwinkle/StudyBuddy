from django.shortcuts import render, redirect,get_object_or_404
from .models import Message
from django.db.models import Q
from django.contrib.auth.models import User

def chat_page(request, username):
    current_user = request.user
    receiver = get_object_or_404(User, username=username)

    messages = Message.objects.filter(
        Q(sender=current_user, receiver=receiver) |
        Q(sender=receiver, receiver=current_user)
    ).order_by('timestamp')

    return render(request, 'chatting_page.html', {'messages': messages, 'receiver': receiver})

def send_message(request, username):
    if request.method == 'POST':
        content = request.POST.get('content')
        sender = request.user
        receiver = get_object_or_404(User, username=username)
        message = Message(sender=sender, receiver=receiver, content=content)
        message.save()
    return redirect('chat_page', username=username)

