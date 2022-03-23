from django import forms
from .models import Post, Comment
from django.utils.translation import gettext_lazy as _


class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [_('body')]


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [_('body')]
        widgets = {
            'body': forms.TextInput(attrs={'class': 'form-control mt-2'})
        }
        labels = {
            "body": "Comment"
        }


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [_('body')]


class PostSearchForm(forms.Form):
    search = forms.CharField()
