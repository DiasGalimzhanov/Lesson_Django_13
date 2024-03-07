from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import News
from .forms import NewsForm


class ListNews(ListView):
    model = News
    template_name = 'home.html'
    context_object_name = 'news'

class CreateNews(CreateView):
    model = News
    template_name = 'create.html'
    form_class = NewsForm
    success_url = reverse_lazy('home')