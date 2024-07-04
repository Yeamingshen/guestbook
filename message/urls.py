from django.urls import path
from . import views

urlpatterns = [
    #空路徑,也就是留言列表(message/    )
    path('', views.MessageList.as_view(), name = 'msg_list'), 

]