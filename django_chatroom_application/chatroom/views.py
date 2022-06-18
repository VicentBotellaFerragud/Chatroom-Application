from django.shortcuts import render
from .models import Chat, Message

# Create your views here.

def index(request):  
    if request.method == 'POST' and request.POST['textMessage'] != '':
        print('method was post', request.POST['textMessage'])
        chat = Chat.objects.get(id = 1)        
        Message.objects.create(text=request.POST['textMessage'], chat = chat, author = request.user, receiver = request.user)

    chatMessages = Message.objects.filter(chat__id = 1)
    return render(request, 'chatroom/index.html', {'chatMessages': chatMessages})