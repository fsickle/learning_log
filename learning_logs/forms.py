from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    # 根据哪个模型创建表单，以及表单只包含text，不为字段生成标签
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

