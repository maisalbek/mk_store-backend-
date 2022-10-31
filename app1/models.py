from cgitb import text
from turtle import title
from typing import Text
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Product(models.Model):
    images = ArrayField(models.CharField(max_length=300, blank=True))
    colors = ArrayField(models.CharField(max_length=300, blank=True))
    color = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    oldprice = models.IntegerField()
    article = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    material = models.CharField(max_length=50)
    textile = models.CharField(max_length=50)
    collection = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Footer(models.Model):
    footerlogo = models.CharField(max_length=300)
    footerText = models.CharField(max_length=100)
    footerTel1 = models.CharField(max_length=20)
    footerTel2 = models.CharField(max_length=20)
    mail = models.EmailField(max_length=50)
    instagram = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    whatsApp = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Footer store"


class Header(models.Model):
    headerLogo = models.CharField(max_length=300)
    headerTel = models.CharField(max_length=20)
    telegram = models.CharField(max_length=100)
    whatsApp = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Header store"


class Slider(models.Model):
    text1 = models.CharField(max_length=50)
    text2 = models.CharField(max_length=50)
    text3 = models.CharField(max_length=50)
    text4 = models.CharField(max_length=50)
    img = models.CharField(max_length=300)
    discount = models.IntegerField(max_length=60)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Slider store"


class Advantages(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Advantages store"


class About(models.Model):
    img1 = models.CharField(max_length=300)
    img2 = models.CharField(max_length=300)
    img3 = models.CharField(max_length=300)
    text = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "About store"


class News(models.Model):
    img = models.CharField(max_length=300)
    headerText = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "News store"


class Help(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Help store"


class publicOffer(models.Model):
    paragraph1 = models.CharField(max_length=1000)
    paragraph2 = models.CharField(max_length=1000)
    paragraph3 = models.CharField(max_length=1000)
    paragraph4 = models.CharField(max_length=1000)
    paragraph5 = models.CharField(max_length=1000)
    paragraph6 = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "PublicOffer store"