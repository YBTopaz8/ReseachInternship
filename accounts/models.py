from django.db import models

# Create your models here.

class Invitation_Tables (models.Model):
    inv_code = models.CharField( max_length=50)
    inv_code_date = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.inv_code
    class Meta:
        verbose_name_plural = "Invitation Table"
        

class Users_Table(models.Model):
    FK_inv_code = models.OneToOneField(Invitation_Tables, on_delete=models.CASCADE)
    username = models.CharField( max_length=50)
    firstname= models.CharField( max_length=50)
    lastname = models.CharField( max_length=50)
    password = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    sign_in_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname + self.lastname
    class Meta:
        verbose_name_plural = "Users Table"
