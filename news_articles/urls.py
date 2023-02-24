from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='news'),
    path('article/<int:pk>/', views.article, name='article'),
    path('addnews/', views.add_news_article, name='add_article'),
    path('editnews/<int:pk>/', views.edit_article, name='edit_article'),
    path('deletenews/<int:pk>/', views.delete_article, name='delete_article'),
]
