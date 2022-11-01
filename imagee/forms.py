from cProfile import label
from django import forms
from .models import ImageUpload

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = '__all__'
        labels = {'photo':''}