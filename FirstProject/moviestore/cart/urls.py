from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name = 'cart.index'),
  path('<int:id>/add', views.add_to_cart, name = 'cart.add'),
]