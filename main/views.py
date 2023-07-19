from django.shortcuts import render
from django.http import HttpResponse
from .models import  Post
from django.urls import reverse
from .forms import CategoryForm, CustomUserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.views.generic  import CreateView
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def logged(request):
    all=Post.objects.filter(author__id=request.user.id)


    context={
        
        'all':all
    }
    return render(request,'blog/logged.html',context)






def about(request):
   return render(request,'blog/about.html')

def profile(request):
   return render(request,'blog/profile.html')

def logout(request):
   return render(request,'blog/logout.html')

def home(request):
   return render(request,'blog/home.html')


def register(request):
    if request.method == "GET":
        return render(
            request, "blog/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("login"))
        


@login_required
def PostDetail(request,pk):
    post_detail=Post.objects.filter(pk=pk)
    context = {'post_detail':post_detail}
    return render (request,"blog/post_detail.html",context)



def add_blog(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST,request.FILES)
        if category_form.is_valid():
            category_form.save()
    category_form = CategoryForm()
    categorys = Post.objects.all()
    addblog=Post.objects.all()
    return render(request,'blog/add_blog.html', context={"category": categorys, "category_form": category_form,'addblog':addblog})




def update_addblog(request,id):
    instance=Post.objects.get(id=id)
    if request.method=="POST":
        category_form=CategoryForm(request.POST,instance=instance)
        if category_form.is_valid():
            category_form.save()
        return redirect('logged')
    category_form=CategoryForm(instance=instance)
    addblog=Post.objects.filter(author__id=request.user.id)
    return render(request,'blog/update_addblog.html',context={'addblog':addblog,"category_form": category_form})



def delete_addblog(request,id):
    adb=Post.objects.get(id=id)
    adb.delete()
    return redirect('logged')

