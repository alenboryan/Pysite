from datetime import timezone
import datetime
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


class PyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)


    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)
    
    
class Info(models.Model):
    title = models.CharField('title', max_length = 50)
    anons = models.CharField('anons', max_length = 50)
    date = models.DateTimeField("date")
    
    def __str__(self):
        return self.title
    
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class Pysintax(models.Model):
    content = models.CharField(max_length=3000)
    
class DjangoInfo(models.Model):
    content = models.CharField(max_length=3000)
    
class Studying(models.Model):
    title = models.CharField(max_length=500, default=None)
    content = models.CharField(max_length=5000, default='')
    
    def __str__(self):
        return self.content

class FlaskInfo(models.Model):
    content = models.CharField(max_length=5000)