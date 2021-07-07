from django.urls import path
from . import views
urlpatterns = [
    path('',views.course_list, name="courses"),
    path('<slug:category_slug>/<int:course_id>',views.course, name="course"),
    path('categories/<slug:category_slug>',views.category, name="category"),
    path('tags/<slug:tag_slug>',views.tag, name="tag"),
    path('search/',views.search, name="search"),

]
