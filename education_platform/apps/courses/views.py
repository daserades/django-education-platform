from django.shortcuts import render
from .models import Course,Category,Tag

def course_list(request):
    
    categories = Category.objects.all()
    tags = Tag.objects.all()
    current_user =request.user
    if current_user.is_authenticated:
        enrolled_course =current_user.courses_join.all()
        courses =Course.objects.all().order_by('-date')
        for course in enrolled_course:
            courses= courses.exclude(id=course.id)

    else:
        courses =Course.objects.all().order_by('-date')

    context = { 
        'courses':courses,
        'categories':categories,
        'tags':tags
    }

    return render(request,'courses/courses.html',context)


def course(request, category_slug, course_id):
    courses =Course.objects.all().order_by('-date')
    current_user =request.user
    course = Course.objects.get(category__slug=category_slug, id= course_id)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    if current_user.is_authenticated:
        enrolled_courses =current_user.courses_join.all()
    else:
        enrolled_courses=courses

    context = {
        'course':course,
        'enrolled_courses': enrolled_courses,
        'categories':categories,
        'tags':tags,
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

