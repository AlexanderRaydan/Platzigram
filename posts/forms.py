""" post form """

#esta es otra forma de hacer los formularios de django
#se crea un formulario general y el código queda mas elegante

#django 
from django import forms

#models
from posts.models import Post

class PostForm(forms.ModelForm):

    class Meta:

        model = Post
        fields = ('user' , 'profile' , 'title' , 'photo')
