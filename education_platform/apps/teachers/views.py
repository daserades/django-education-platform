from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Teacher
from ..courses.models import Course


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/teachers.html'
    context_object_name= 'teachers'
    paginate_by=3


class TeacherDetailView(DetailView):
    model = Teacher
    template_name= 'teachers/teacher.html'
    context_object_name= 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses']= Course.objects.filter(available=True, teacher = self.kwargs['pk'])
        return context
