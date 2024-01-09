from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=200,verbose_name="Students name")
    email=models.EmailField(max_length=200,verbose_name="Students email")
    def __str__(self):
        return str(self.id)
        

# Create your models here.
