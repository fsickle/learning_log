from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    # 根据哪个模型创建表单，以及表单只包含text，不为字段生成标签
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        # 覆盖 django 默认的小部件:制定 text 输入的小部件宽度设置为 80，而不是40默认
        widgets = {'text':forms.Textarea(attrs={'cols':80})}
        
