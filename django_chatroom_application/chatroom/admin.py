from django.contrib import admin
from .models import Chat, Message

class ChatAdmin(admin.ModelAdmin):
    fields = ('created_at',)
    list_display = ('created_at',)

class MessageAdmin(admin.ModelAdmin):    
    fields = ('created_at', 'chat', 'author', 'text', 'receiver')    
    list_display = ('created_at', 'chat', 'author', 'text', 'receiver')    
    search_fields = ('text',)

# Register your models here.

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)