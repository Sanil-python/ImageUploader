from tkinter import Image
from django.shortcuts import render

from imagee.models import ImageUpload
from .forms import ImageForm

# Create your views here.

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    form = ImageForm()
    img = ImageUpload.objects.all()
    return render(request, 'imagee/home.html', {'img':img, 'form':form})