from django.db import models

# Create your models here.
class Message(models.Model):
    user = models.CharField('留言者', max_length = 30)
    receipt = models.CharField('留言對象', max_length = 30)
    subject = models.CharField('主題', max_length = 60)
    content = models.TextField('內容')
    created = models.DateTimeField('留言時間', auto_now_add = True)#auto_now_add代表會在留言時自動記錄日期
    #updated = models.DateTimeField('最後修改時間', auto_now = True)#auto_now代表會更新資料時間，在修改時不會動到auto_now_add但會動到auto_now

    