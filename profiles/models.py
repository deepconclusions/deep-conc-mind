from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Qualification(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    gender = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profiles/')
    bio = models.TextField()
    skills = models.ManyToManyField(to=Skill)
    qualifications = models.ManyToManyField(to=Qualification)

    def __str__(self):
        return self.name