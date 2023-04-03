from django.shortcuts import render

# Create your views here.
from .models import Post





from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView , UpdateView ,DeleteView
class PostList(ListView):
    model = Post
    
class PostDetail(DetailView):
    model = Post
class PostCreate(CreateView):
    model = Post
    fields= ['title','content','image']
    success_url = '/blog/'



class PostEdit(UpdateView):
    model = Post
    fields= ['title','content','image']
    success_url = '/blog/'



class PostDelete(DeleteView):
    model = Post
    success_url = '/blog/'

