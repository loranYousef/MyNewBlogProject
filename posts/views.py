from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    all =Post.objects.all()
    return render(request,'qq.html',{'data':all})


#def post_detail(request):


#def post_create(request):


#def post_edit(request):


#def post_deletee(request):
