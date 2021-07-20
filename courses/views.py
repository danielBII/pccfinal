from django.shortcuts import render
from .models import Courses

def course_unique(request, slug):
    try:
        course = Courses.objects.get(slug=slug)
    except Exception as err:
        print(err)
    context = {
        'course': course
    }

    return render(request, 'course.html', context)