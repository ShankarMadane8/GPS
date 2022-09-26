from django.contrib import admin
from .models import Register,Images
# Register your models here.

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
  list_display=("first_name","last_name","email","password","confirm_password")

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
  list_display=("img",)
    


    

