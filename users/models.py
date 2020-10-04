from django.db import models
from django.contrib.auth.models import User #modelo de usuario de django

class Profile(models.Model):

    user = models.OneToOneField(User, related_name='profile' , on_delete= models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank= True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(upload_to = 'user/pictures' , blank = True , null = True)

    created = models.DateTimeField(auto_now_add= True)
    modified = models.DateTimeField(auto_now=True)

    followers = models.IntegerField( blank=True , null= True )
    following = models.IntegerField( blank=True , null= True )


    def __str__(self):

       return self.user.last_name #se marca como rojo pero corre fresco, npi que pasa



class Contact(models.Model):

    user_from = models.ForeignKey(User , related_name= 'rel_from_set' , on_delete = models.CASCADE)
    user_to = models.ForeignKey(User , related_name= 'rel_to_set', on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add= True , db_index= True)

    class Meta:

        ordering = ('-created',)


User.add_to_class('following' , models.ManyToManyField('self' , through=Contact , related_name= 'followers' , symmetrical= False))