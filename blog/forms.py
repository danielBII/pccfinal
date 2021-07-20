from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input'}))
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ('title','text','img')
        