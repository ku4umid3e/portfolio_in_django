from django import views
from django.urls import path, include

from .views import all_blogs, detail

urlpatterns = [
    path('', all_blogs, name='all_blogs'),
    path('<int:blog_id>/', detail, name='detail')
]