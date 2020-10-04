"""Posts Model"""

#django
from django.db import models

from django.contrib.auth.models import User

from users.models import Profile

class Post(models.Model):

    #ASÍ LO RELACIONAMOS CON LAS LLAVES FORANEAS
    user = models.ForeignKey(User , on_delete = models.CASCADE) #RELACIONAMOS EL POST CON EL USUARIO
    profile = models.ForeignKey(Profile , on_delete= models.CASCADE) #RELACIONAMOS EL POST CON EL PERFIL

    title = models.CharField(max_length=255 , null= False , blank= False)
    photo = models.ImageField(
        upload_to = 'posts/photos' , # en este path de nuestro proyecto guardará las fotos
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now= True)

    def __str__(self):

        return '{} by @{}'.format(self.title , self.user.username) #no sé por que marca rojo, el server corre fresco