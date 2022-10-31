from django.shortcuts import render
from rest_framework import viewsets
from .models import About, Advantages, Header, Help, News, Product, Footer, Slider, publicOffer
from .serializers import AboutSerializer, AdvantagesSerializer, HeaderSerializer, HelpSerializer, NewsSerializer, ProductSerializer, SliderSerializer, UserSerializer, FooterSerializer, publicOfferSerializer
from django.contrib.auth.models import User


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
        
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FooterViewset(viewsets.ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer

class HeaderViewset(viewsets.ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer

class SliderViewset(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

class AdvantagesViewset(viewsets.ModelViewSet):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer

class AboutViewset(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class NewsViewset(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class HelpViewset(viewsets.ModelViewSet):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer

class publicOfferViewset(viewsets.ModelViewSet):
    queryset = publicOffer.objects.all()
    serializer_class = publicOfferSerializer