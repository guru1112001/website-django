from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import (ListView)
from .models import blogs
# Create your views here.
class bloglistview(ListView):
    model = blogs
    template_name ='home.html'
    context_object_name = 'blog'
# Create your views here.
