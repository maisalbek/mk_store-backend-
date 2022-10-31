from django.urls import path, include
from .views import AboutViewset, AdvantagesViewset, FooterViewset, HelpViewset, NewsViewset, ProductViewset, SliderViewset, UserViewset, HeaderViewset, publicOfferViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products', ProductViewset, basename='products')
router.register('users', UserViewset, basename='users')
router.register('footer', FooterViewset, basename='footer')
router.register('header', HeaderViewset, basename='header')
router.register('slider', SliderViewset, basename='slider')
router.register('advantages', AdvantagesViewset, basename='advantages')
router.register('about', AboutViewset, basename='about')
router.register('news', NewsViewset, basename='news')
router.register('help', HelpViewset, basename='help')
router.register('publicoffer', publicOfferViewset, basename='publicoffer')

urlpatterns = [
    path('', include(router.urls))
]
