from django.urls import path, include

from .views import all_blogs

urlpatterns = [
    path('', all_blogs, name='all_blogs'),
]