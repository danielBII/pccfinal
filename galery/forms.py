from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Galery


class GaleryForm(forms.ModelForm):

    class Meta:
        model = Galery
        fields = ('name','description','img',)