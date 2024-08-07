from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.

def welcome(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()

    img = Image.objects.all()
    return render(request, 'myapp/welcome.html', {'img': img, 'form': form})