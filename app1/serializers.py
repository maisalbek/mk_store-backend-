from .models import About, Advantages, Header, Help, News, Product, Footer, Slider, publicOffer
from rest_framework import serializers
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'images','colors','color','title','price','oldprice','description','material','textile','collection','type', 'created', 'updated']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'created', 'updated']

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['id', 'footerlogo', 'footerText', 'footerTel1', 'footerTel2', 'mail', 'instagram', 'telegram', 'whatsApp', 'created', 'updated']

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ['id', 'headerLogo', 'headerTel', 'telegram', 'whatsApp', 'created', 'updated']

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'text1', 'text2', 'text3', 'text4', 'img', 'discount', 'created', 'updated']

class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = ['id', 'title', 'text', 'created', 'updated']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'img1', 'img2', 'img3', 'text', 'created', 'updated']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'img', 'headerText', 'text', 'created', 'updated']

class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ['id', 'question', 'answer', 'created', 'updated']

class publicOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = publicOffer
        fields = ['id', 'paragraph1', 'paragraph2', 'paragraph3', 'paragraph4', 'paragraph5', 'paragraph6', 'created', 'updated']
