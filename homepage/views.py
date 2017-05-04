from django.views import generic
from .models import *


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class BlogView(generic.ListView):
    model = Blog
    context_object_name = 'all_blog'
    template_name = 'blog.html'


class DetailView(generic.DetailView):
    model = Blog
    template_name = 'details.html'
    context_object_name = 'detail'


class AboutView(generic.TemplateView):
    template_name = 'about.html'
