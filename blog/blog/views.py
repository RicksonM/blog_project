from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from blog.models import Post

# Create your views here.

class ListPost(ListView):
    model = Post
    template_name = "index.html"

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset


class PostDetail(DetailView):
    model = Post
    template_name = "post.html"


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'text']
    template_name = "post_form.html"
    success_url = "/"