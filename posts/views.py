#django
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


#model
from posts.forms import PostForm
from posts.models import Post


def Post_detail_view(request , post_id):

    post = Post.objects.get(pk = post_id)

    return render(request = request ,template_name= 'posts/detail.html' , context = {'post': post})



@login_required
def list_posts(request):

    posts = Post.objects.all().order_by('-created')

    return render(request = request ,template_name= 'posts/feed.html' , context = {'posts': posts})


@login_required
def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()

            return redirect('feed')
        
    else :

        form = PostForm()

    return render(

        request= request ,
        template_name= 'posts/new.html',
        context= {
            'form' :form ,
            'user' : request.user ,
            'profile' : request.user.profile
        },
    )

