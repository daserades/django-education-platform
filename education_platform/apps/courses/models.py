from django.db import models
from django.db.models.base import ModelState
from ..teachers.models import Teacher
class Category(models.Model):
    name=models.CharField(max_length=100,null=True)
    slug=models.SlugField(max_length=50,null=True, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100,null=True)
    slug=models.SlugField(max_length=50,null=True, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=250,unique=True, verbose_name="Course Name")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="courses/%Y%m%d/",default="courses/default.jpg")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    tags =models.ManyToManyField(Tag, blank=True, null =True)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

