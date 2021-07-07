from django.shortcuts import render
from .models import Course,Category,Tag

def course_list(request):
    courses =Course.objects.all().order_by('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = { 
        'courses':courses,
        'categories':categories,
        'tags':tags
    }

    return render(request,'courses/courses.html',context)


def course(request, category_slug, course_id):
    course = Course.objects.get(category__slug=category_slug, id= course_id)
    context = {
        'course':course
    }
    return render(request,'courses/course.html',context)

def category(request,category_slug):
    courses = Course.objects.all().filter(category__slug=category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
       'courses':courses,
       'categories':categories,
       'tags':tags
    }
    return render(request,'courses/courses.html',context)

def tag(request, tag_slug):
    courses =Course.objects.all().filter(tags__slug=tag_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
       'courses':courses,
       'categories':categories,
       'tags':tags
    }
    return render(request,'courses/courses.html',context)

def search(request):
    courses =Course.objects.filter(name__contains = request.GET['search'])
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
       'courses':courses,
       'categories':categories,
       'tags':tags
    }
    return render(request,'courses/courses.html',context)