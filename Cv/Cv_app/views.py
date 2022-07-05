from django.contrib import messages
from django.shortcuts import render, redirect
from Cv_app.forms import CvForm
from Cv_app.models import Cv


# add contact details  to database
def add(request):
    if request.method == 'POST':
        form = CvForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'ok')
            return redirect('/')
    else:
        form = CvForm()
    return render(request, 'add.html', {'form': form})


# update data in database
def update(request, id):
    move = Cv.objects.get(id=id)
    form = CvForm(request.POST or None, request.FILES, instance=move)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'move': move})


# display data in detail
def display(request, cv_id):
    cv = Cv.objects.get(id=cv_id)
    return render(request, 'index.html', {'cv': cv})


# display home screen
def home(request):
    cv = Cv.objects.all()
    context = {'cv': cv}
    return render(request, 'thumbnail.html', context)
