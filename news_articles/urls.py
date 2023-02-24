from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='news'),
    path('article/<str:pk>', views.article, name='article'),
    path('addnews/', views.add_news_article, name='add_article'),
]
