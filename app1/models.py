from django.db import models

# Create your models here.


class Services(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField(max_length=300)
    slug = models.CharField(max_length=300)
    image = models.ImageField(upload_to="service/")
    objects = models.Manager()

    def __str__(self):
        return self.title


class AboutSect(models.Model):
    image = models.ImageField(upload_to="about/")
    objects = models.Manager()
    title = models.CharField(max_length=300)
    text = models.TextField(max_length=300)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    image = models.ImageField(upload_to="team/")
    objects = models.Manager()

    def __str__(self):
        return self.name


class Customers(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    image = models.ImageField(upload_to="team/")
    objects = models.Manager()

    text = models.TextField()

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    image = models.ImageField(upload_to="about/")
    title = models.CharField(max_length=200)
    text = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return self.title
