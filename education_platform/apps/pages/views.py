from .forms import ContactForm
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from ..courses.models import Category, Course
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from ..teachers.models import Teacher

class AboutView(TemplateView):
    template_name='pages/about.html'

class IndexView(TemplateView):
    template_name='pages/index.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['courses'] =Course.objects.filter(available=True).order_by('-date')[:4]
        context['total_course']= Course.objects.filter(available=True).count()
        context['categories'] =Category.objects.all()
        context['total_students'] =User.objects.count()
        context['total_teachers'] =Teacher.objects.count()
        return context

class ContactView(SuccessMessageMixin,FormView):
    template_name='pages/contact.html'
    form_class =ContactForm
    success_url = reverse_lazy('contact')
    success_message ='We received your request'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)




