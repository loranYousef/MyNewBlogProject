from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    all =Post.objects.all()
    return render(request,'qq.html',{'data':all})



def post_detail(request,id):
     post = Post.objects.get(id=id)
     return render(request,'single.html',{'data':post})


def post_create(request):
    if request.method =='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    
    form =PostForm()
    return render(request,'create.html',{'form':form})


#def post_edit(request):


#def post_deletee(request):
