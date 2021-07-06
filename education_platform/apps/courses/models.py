from django.db import models
from django.db.models.base import ModelState

class Course(models.Model):
    name = models.CharField(max_length=250,unique=True, verbose_name="Course Name")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="courses/%Y%m%d/",default="courses/default.jpg")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

