from django.shortcuts import redirect, render
from .models import NewBlog
from . import forms

# Create your views here.

def blogHome (request):
    blogs = NewBlog.objects.all()
    return render(request, "blog/blogHome.html", {'blogs' : blogs})

def post (request):    
    return render(request, "blog/post.html")

def font (request):    
    return render(request, "blog/font.html")

# def addBlog (request):
#     return render(request, "blog/addBlog.html")

def business (request):
    return render(request, "blog/business.html")

def blogNew(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("blogHome")
    else:
        form = forms.CreatePost()
    return render(request, 'blog/addBlog.html', {'form' : form})

def blogDetails(request, pk):
    blog = NewBlog.objects.get(pk=pk)
    return render(request, "blog/blogDetails.html", {"blog": blog})