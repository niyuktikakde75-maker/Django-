from django.urls import path
from . import views

urlpatterns = [
    path('addtocart',views.addtocart),
   
]