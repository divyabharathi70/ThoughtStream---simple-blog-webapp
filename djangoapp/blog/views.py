from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Post
from django.http import Http404
from blog.form import Contact
from django.contrib import messages

# posts = [
#           {'id':1,'posttitle':'Post1' ,'content':'Post 1 Content'},
#           {'id':2,'posttitle':'Post2' ,'content':'Post 2 Content'},
#           {'id':3,'posttitle':'Post3' ,'content':'Post 3 Content'},
#           {'id':4,'posttitle':'Post4' ,'content':'Post 4 Content'},
#      ]

def index(request):
     title = "Latest Posts..."
     blogtitle = "blog"
     posts = Post.objects.all()
     return render(request,'blog/index.html',{'title':title,'blogtitle':blogtitle,'posts':posts})

def detail(request,slug):
     # post = next((post for post in posts if post['id'] == int(id)) , None)
     try:
       post = Post.objects.get(slug = slug)
       relatedposts = Post.objects.filter(category = post.category).exclude(id= post.id)
     except:
         raise Http404("Post not Found")
     return render(request,'blog/detail.html',{'post':post,'relatedposts':relatedposts})

def contact(request):
     if request.method=='POST':
         form = Contact(request.POST)

     return render(request,'blog/contact.html')
    
def about(request):
    return render(request,'blog/about.html')