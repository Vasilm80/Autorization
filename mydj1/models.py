from django.db import models

# Create your models here.
class Testm(models.Model):
    log = models.CharField(max_length=50, verbose_name='Login')
    pas = models.CharField(max_length=50, verbose_name='Password')





class UserModel(models.Model):
    log = models.CharField(max_length=100, verbose_name='Login')
    pas = models.CharField(max_length=150, verbose_name='Password')
    email = models.CharField(max_length=200, verbose_name='E-mail')