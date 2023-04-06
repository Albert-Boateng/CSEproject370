from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('comments_reviews/', views.view_index),
    path('cart/', views.cart),
    path('thank_you/', views.thank_you),
]