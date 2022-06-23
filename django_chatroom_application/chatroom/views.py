from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Chat, Message
from django.http import HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

"""
Redirects the user to the chatroom view as soons as the app loads.
"""
def redirectToChatroom(request):
    
    response = redirect('/chatroom/') # I could have used 'HttpResponseRedirect' a well. There's no difference.
    
    return response

"""
Renders the login view and logs in the user if he/she fulfills the if conditions.
"""
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

"""
Renders the register view and registers the user if he/she fulfills the if conditions.
"""
def registerFn(request):
    
    newUsername = request.POST.get('newUsername')
    newPassword = request.POST.get('newPassword')
    repeatPassword = request.POST.get('repeatPassword')

    if request.method == 'POST':
        
        if newUsername != '' and newPassword != '' and repeatPassword !='': 

            if newPassword == repeatPassword: 

                try: 
                    user= User.objects.get(username = newUsername)
                    return render(request, 'auth/register-view.html', {'usernameAlreadyExists': True})  

                except User.DoesNotExist: 
                    user = User.objects.create_user(username = newUsername, password = newPassword)
                    user.save()
                    return HttpResponseRedirect('/login/') 

            else:

                return render(request, 'auth/register-view.html', {'passwordsDifferent': True})

        else:
            return render(request, 'auth/register-view.html', {'anyFieldEmpty': True})

    
    return render(request, 'auth/register-view.html')

"""
Renders the chatroom view. It also creates and stores in the database the messages that the user types and returns them in json format.
"""
@login_required(login_url = '/login/')
def index(request):  
    
    if request.method == 'POST' and request.POST['textMessage'] != '':
        chat = Chat.objects.get(id = 1)        
        newMessage = Message.objects.create(text = request.POST['textMessage'], chat = chat, author = request.user, receiver = request.user)
        newMessageSerialized = serializers.serialize('json', [ newMessage, ])
        return JsonResponse(newMessageSerialized[1:-1], safe = False)

    chatMessages = Message.objects.filter(chat__id = 1)
    
    return render(request, 'chatroom/index.html', {'chatMessages': chatMessages})

"""
Renders the logout view and logs out the user.
"""
def logoutFn(request):
    
    logout(request)

    return render(request, 'auth/logout-view.html')