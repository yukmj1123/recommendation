from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def post_list(request):
    posts = Post.objects.all()

    return render(request, 'post_list.html',{
        'posts': posts,
    })
def post_detail(request, post_id):
    post = Post.objects.get(id = post_id)

    post.save()

    return render(request, 'post_detail.html',{
        'post': post,
    })

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post =form.save()

            return redirect('post_detail',post.id)
    else:
        form=PostForm()

        return render(request, 'post_new.html',{
            'form':form,
        })
