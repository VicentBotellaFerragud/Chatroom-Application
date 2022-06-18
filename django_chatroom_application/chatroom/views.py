from asyncio.windows_events import NULL
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Chat, Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def redirectToChatroom(request):
    response = redirect('/chatroom/')
    return response

@login_required(login_url = '/login/')
def index(request):  
    if request.method == 'POST' and request.POST['textMessage'] != '':
        print('method was post', request.POST['textMessage'])
        chat = Chat.objects.get(id = 1)        
        Message.objects.create(text = request.POST['textMessage'], chat = chat, author = request.user, receiver = request.user)

    chatMessages = Message.objects.filter(chat__id = 1)
    return render(request, 'chatroom/index.html', {'chatMessages': chatMessages})

def loginFn(request):
    redirect = request.GET.get('next')
    if request.method == 'POST':
        user = authenticate(username = request.POST['username'], password = request.POST['password'])

        if user:
            login(request, user)

            if redirect:
                return HttpResponseRedirect(request.POST.get('next'))
            else:
                return HttpResponseRedirect('/chatroom/')
        
        else:
            return render(request, 'auth/login-view.html', {'wrongPassword': True, 'redirect': redirect})

    return render(request, 'auth/login-view.html', {'redirect': redirect})

def logoutFn(request):
    logout(request)
    return render(request, 'auth/logout-view.html')

def registerFn(request):
    
    newUsername = request.POST.get('newUsername')
    newPassword = request.POST.get('newPassword')
    repeatPassword = request.POST.get('repeatPassword')

    if request.method == 'POST':
        user = User.objects.create_user(newUsername, '', newPassword)
        user.save()
        return HttpResponseRedirect('/login/')

    
    return render(request, 'auth/register-view.html')