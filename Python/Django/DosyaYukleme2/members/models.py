from django.db import models

#securityint güvenliği sağlamak için ikinci anahtar
class Members(models.Model):
    user = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    ePosta = models.CharField(max_length=255)
    Securityint = models.IntegerField()

class File(models.Model):
    user = models.CharField(max_length=255)
    category = models.SmallIntegerField()
    fileType = models.SmallIntegerField()
    fileName = models.CharField(max_length=255)
    file = models.FileField()
    date = models.DateField()
    info = models.CharField(max_length=255)

# Create your models here.
