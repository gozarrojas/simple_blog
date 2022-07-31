from django import forms
from comments.models import Comment


class CreateCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ('user', 'profile', 'post', 'comment')
