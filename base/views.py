from .forms import ImageForm, PostForm
from django.shortcuts import render, redirect
from base.models import Post, Images
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
# posts = [
#     {'id':1, 'name':'aaaaaa'},
#     {'id':2, 'name':'bbbbbb'},
#     {'id':3, 'name':'cccccc'},
# ]

def home(request):
    posts = Post.objects.all()
    context={'posts':posts}
    return render(request, 'base/home.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    images = Images.objects.filter(post=post)
    context={'post': post,'images': images}   
    return render(request, 'base/post.html' , context)    

# to do wyjabania ale mozna skorzytac dla dizajnu
def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = Images.objects.filter(post=post)
    return render(request, 'base/photos.html', {
        'post':post,
        'photos':photos
    })



def createPost(request):
    form = PostForm(request.POST or None,request.FILES or None)
    image = request.FILES.getlist("images")
    if request.method == "POST":
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            for i in image:
                Images.objects.create(post=f, images=i)
            messages.success(request, "New Post Added")
            return HttpResponseRedirect("/") 
    else:        
        image_form=ImageForm()
        form=PostForm()
    context = {'form':form,'image_form':image_form}      
    return render(request,'base/post_form.html', context)




# def createPost(request):
#     form = PostForm()
#     if request.method == "POST":
#         images = request.FILES.getlist('images')
#         for image in images:
#             photo = Post.objects.create(image=image,)
#             form = PostForm(request.POST)
#             if form.is_valid():
#              form.save()
#              photo.save()
#     context = {'form':form}
#     return render(request, 'base/post_form.html',context)