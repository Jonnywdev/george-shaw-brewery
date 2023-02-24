from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='news'),
    # path('<slug:slug>/', views.PostList.as_view(), name='article'),
]