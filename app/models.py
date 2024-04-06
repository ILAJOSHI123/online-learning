from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.db import models



# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    concern = models.TextField()
   





# Create your models here.
