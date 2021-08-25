from django.shortcuts import render,HttpResponse,redirect
from .forms import PostForm,RegisterForm
import datetime
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
def HomePage(request):
    user_post=Post.objects.filter(user=request.user)
    #print(user_post)
    post_list = []

    for i in user_post:
        post_list.append(i)

    return render(request,'user/HomePage.html',{'post_list':post_list})

def Logout(request):
    logout(request)
    return redirect('LoginUser')

def LoginUser(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        print(User.objects.all())


        user = User.objects.get(username=username,password=password)
        print(user)

        if user is not None:
                login(request, user)
                return redirect('HomePage')
        else:
            print(user)



    return render(request,'user/LoginUser.html')



def RegisterUser(request):
    form=RegisterForm()

    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LoginUser')

    return render(request,'user/RegisterUser.html',{'form':form})

def AddPost(request):

    if request.method=="POST":
        form=PostForm(request.POST)
        new_form = form.save(commit=False)
        new_form.user = request.user
        #new_form.update_at=datetime.datetime.now()
        new_form.save()
        return redirect('HomePage')
        # if form.is_valid():
        #     form.save()

    else:
        form=PostForm()


    return render(request,'user/AddPost.html',{'form':form})

def EditPost(request,id):

    post=Post.objects.get(id=id)
    form=PostForm(instance=post)

    print(post)

    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('HomePage')

    return render(request,'user/Editpost.html',{'form':form,'id':id})

def DeletePost(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return redirect('HomePage')
