from django.shortcuts import render, redirect
from .models import Course
import datetime

def index(request):
    # Course.objects.create(name='How to fly', description='like an eagle')
    # courses = Course.objects.all()
    # for course in courses:
    #     print course.id, '-', course.name, '-', course.description, '-', course.date_added.strftime('%b %d, %Y %-I:%M%p')
    context = {'courses': Course.objects.all().order_by('-date_added')}
    return render(request, 'courses/index.html', context)

def remove(request, num):
    context = {'courses': Course.objects.get(id=num)}
    return render(request, 'courses/destroy.html', context)

def confirm(request, num):
    Course.objects.get(id=num).delete()
    return redirect('/')

def create(request):
    name = request.POST['name']
    description = request.POST['description']
    if len(name) < 1 or len(description) < 1:
        return redirect('/')

    Course.objects.create(name=name, description=description)
    return redirect('/')
