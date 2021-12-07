from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Comment, Lesson, Reply

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        # fields = ("__all__")
        fields = ('lesson_id', 'name', 'position','video','ppt','notes')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        labels = {"body":"Comment:"}

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control','row':4,'cols':70,'placeholder':"Enter Your Comment"}),
        }

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request',None)
    #     super(CommentForm, self).__init__(*args,**kwargs)

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_body',)

        widgets = {
            'reply_body': forms.Textarea(attrs={'class':'form-control','rows':2,'cols':10}),
        }

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request',None)
    #     super(ReplyForm, self).__init__(*args,**kwargs)