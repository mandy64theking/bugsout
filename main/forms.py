from django import forms
from .models import *
class newPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','description']
class newCommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text']
class feedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['rating','commentid']