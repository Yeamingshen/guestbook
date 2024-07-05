from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Message
from django.urls import reverse_lazy

# Create your views here.
class MessageList(ListView):
    model = Message
    ordering = ['-created']
    #ordering是排序,後面則是放置參考數值
    #在created(或是其他參數)前面加上-號代表反過來
    #自動找 message/message_list.html 作使用

class MessageRead(DetailView):
    model = Message
    #自動找 message/message_detail.html 作使用

class MessageNew(CreateView):
    model = Message
    fields = ['user', 'receipt', 'subject', 'content']
    #fields = '__all__' 可使用時機是在項目很多但要全部欄位顯示的時候，如果是其他情況則像16行一項一項列出
    success_url = reverse_lazy('msg_list')#當成功後回到列表，reverse_lazy會自動回追
    #自動找 message/message_form.html 作使用

class MessageDelete(DeleteView):
    model = Message
    success_url = reverse_lazy('msg_list')#原'/message/'是指定位址，但用reverse_lazy則是追蹤回上頁

    #預設找到 應用程式/資料模型_confirm_delete.html -> message/message_confirm_delete.html
    #範本變數:form, object, 資料模型(小寫)