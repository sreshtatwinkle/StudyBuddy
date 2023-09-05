from django.shortcuts import render, redirect,get_object_or_404
from .models import Message
from django.db.models import Q
from django.contrib.auth.models import User
from django.db.models import Max, F, Case, When, Value, BooleanField
from django.db import models

def chat_page(request, username):
    current_user = request.user
    # user_id = current_user.id  
    receiver = get_object_or_404(User, username=username)

    messages = Message.objects.filter(
        Q(sender=current_user, receiver=receiver) |
        Q(sender=receiver, receiver=current_user) 
    ).order_by('timestamp')
    
    return render(request, 'chatting_page.html', {'messages': messages, 'receiver': receiver})
    

    
  



def chat_room(request):
    current_user = request.user

    users_with_chats = User.objects.filter(
        Q(sent_messages__receiver=current_user) | Q(received_messages__sender=current_user)
    ).distinct()

    users_with_chats = users_with_chats.annotate(
        latest_message_timestamp=Max(
            Case(
                When(sent_messages__receiver=current_user, then='sent_messages__timestamp'),
                When(received_messages__sender=current_user, then='received_messages__timestamp'),
                default=None,
                output_field=models.DateTimeField(),
            )
        )
    )

    users_with_chats = users_with_chats.order_by('-latest_message_timestamp')

    return render(request, 'chat_users_list.html', {'users_with_chats': users_with_chats})

  


    


def send_message(request, username):
    if request.method == 'POST':
        content = request.POST.get('content')
        sender = request.user
        receiver = get_object_or_404(User, username=username)
        message = Message(sender=sender, receiver=receiver, content=content)
        message.save()
    return redirect('chat_page', username=username)

