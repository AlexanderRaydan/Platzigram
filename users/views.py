#django
from django.shortcuts import render , redirect
from django.urls import reverse
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User

from users.forms import ProfileForm
from users.forms import SignupForm

#Users
from users.models import Profile
from users.models import Contact

#posts
from posts.models import Post


@login_required
def user_details(request, username):

    user = User.objects.get(username= username)
    post = Post.objects.filter(user=user).order_by('-created')

    posts_count = post.count()

    exists_conextion = is_following(request.user , user)

    #actualizo los seguidores
    user.profile.followers = Contact.objects.filter(user_to= user).count()
    user.profile.following = Contact.objects.filter( user_from= user).count()

    return render(request ,
        template_name='users/detail.html' ,
        context= {'posts':post ,
        'exists_conextion': exists_conextion ,
        'user':user ,
        'posts_count' : posts_count ,
        } ) 



def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request , username = username, password = password) #autentifica el usuario

        if user:

            login(request , user) #si el usuario y la clave son correctas, se logea
            return redirect('feed')
        else:

            return render(request , 'users/login.html' , {'error': 'Invaid username and password'})

    return render(request , 'users/login.html')


@login_required
def logout_view(request):

    logout(request)
    return redirect('login')


@login_required
def update_profile(request):

    profile = request.user.profile

    form = ProfileForm(request.POST , request.FILES)# el request.FILE es para que se envie la foto de perfil

    if request.method == 'POST':

        if form.is_valid():

            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']

            profile.save()

            url = reverse('user_detail' , kwargs = {'username':request.user.username})

            return redirect(url)


    return render(
        request = request,
        template_name= 'users/update_profile.html' ,
        context={'profile': profile , 'name': request.user , 'form': form } ,
        )
  

def signup(request):

    if request.method == 'POST':

        form = SignupForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')
    else :

        form = SignupForm()

    return render(
        request= request ,
        template_name= 'users/signup.html', 
        context= {'form': form}
        )


@login_required
def user_follow_view(request ,user_to_id ):

    user_from = User.objects.get(pk = request.user.pk)
    user_to = User.objects.get(pk = user_to_id)

    if user_from.pk != user_to.pk: #el usuario no puede seguirse a si mismo

        exist_contact = is_following(user_from , user_to)

        if exist_contact == False: #el usuario no puede seguir 2 veces o mas a la misma persona 

            follow = Contact(user_from = user_from , user_to = user_to)

            follow.save()


    url = reverse('user_detail' , kwargs = {'username': user_to.username})
    return redirect(url)


@login_required
def user_unfollow_view(request ,user_to_id ):

    user_from = User.objects.get(pk = request.user.pk)
    user_to = User.objects.get(pk = user_to_id)

    follow = Contact.objects.get(user_from= user_from , user_to = user_to)

    follow.delete()

    url = reverse('user_detail' , kwargs = {'username': user_to.username})
    return redirect(url)
    

def is_following(user_from ,  user_to):

    exist_contact = Contact.objects.filter(user_from = user_from , user_to = user_to).exists()

    return exist_contact




