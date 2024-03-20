from django.db import models

class db1(models.Model):
    username = models.TextField()    
    email = models.TextField()
    password = models.TextField()
