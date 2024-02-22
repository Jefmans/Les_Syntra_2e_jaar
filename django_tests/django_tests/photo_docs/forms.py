from django import forms
from .models import Image, Document


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file']