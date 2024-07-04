from django.shortcuts import render
from django.views.generic import ListView
from .models import Message

# Create your views here.
class MessageList(ListView):
    model = Message