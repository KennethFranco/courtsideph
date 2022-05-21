from django.urls import path
from . import views
 
urlpatterns = [
   path('', views.home, name = "home"),
   path('catalog', views.catalog, name="catalog"),
   path('card-grading', views.cardgrading, name = "cardgrading"),
   path('marketplace', views.marketplace, name = "marketplace"),
   path('contact-us', views.contactus, name = "contactus")
]
