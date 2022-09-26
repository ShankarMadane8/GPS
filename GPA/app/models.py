from django.db import models

# Create your models here.

class Register(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  email=models.EmailField(unique=True)
  password=models.CharField(max_length=500)
  confirm_password=models.CharField(max_length=500)
  
class Images(models.Model):
  img=models.ImageField(upload_to='upload/')
 