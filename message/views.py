from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Message

# Create your views here.
class MessageList(ListView):
    model = Message
    #自動找 message/message_list.html 作使用

class MessageRead(DetailView):
    model = Message
    #自動找 message/message_detail.html 作使用

class MessageNew(CreateView):
    model = Message
    fields = ['user', 'receipt', 'subject', 'content']
    #fields = '__all__' 可使用時機是在項目很多但要全部欄位顯示的時候，如果是其他情況則像16行一項一項列出
    success_url = '/message/'#當成功後回到列表
    #自動找 message/message_form.html 作使用

class MessageDelete(DeleteView):
    model = Message