#django
from django.db import models

#ESTAS SON LAS CLASES QUE EL ORM LEERÁ PARA CREAR LA BASE DE DATOS

class User(models.Model):

    email = models.EmailField(unique= True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank= True)
    country = models.CharField(max_length=50 , null=True)
    city = models.CharField(max_length=50 , null= True)

    is_admin = models.BooleanField(default=False)

    birthdate = models.DateField(blank= True, null= True)
    created = models.DateTimeField( auto_now_add= True )
    modified = models.DateTimeField(auto_now= True)



    def __str__(self): #para que cuando imprima el nombre, muestre el email

        return self.email


#user = User.objects.get(email = 'freddier@platzi.com') ejemplo de query, deme el usuario cuyo email sea 'freddier@platzi.com'
# platzi_user = User.objects.filter(email__endswith = 'platzi.com').update(is_admin = True)  actualizar
