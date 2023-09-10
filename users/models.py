from django.db import models

# Create your models here.
class User(models.Model):
    user_id= models.AutoField(primary_key=True)
    username= models.CharField(max_length=120)
    password= models.CharField(max_length=120)
    
    def __str__(self):
        return str(self.username)