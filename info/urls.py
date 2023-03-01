from django.urls import path
from . import views

urlpatterns = [
    path('cookie/', views.cookie, name='cookie'),
    path('delivery/', views.delivery, name='delivery'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
]
