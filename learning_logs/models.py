from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    '''用户学习的主题'''
    text = models.CharField(max_length=200)  # 预留200
    date_added = models.DateTimeField(auto_now_add=True) # 自动记录当前时间
    owner = models.ForeignKey(User)
    
    def __str__(self):
        '''返回模型的字符串表示'''
        return self.text

class Entry(models.Model):
    '''学到的某个主题的具体知识'''
    # 取得主题创建时，分配的键（ID）
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    # 存储用于管理模型的额外信息：设置特殊属性，用 Entries 表示多个条目
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        if len(self.text) > 50:
            return self.text[:50] + '...'
        return self.text
