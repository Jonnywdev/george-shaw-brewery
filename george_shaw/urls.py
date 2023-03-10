from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('contact/', include('contact.urls')),
    path('our_story/', include('our_story.urls')),
    path('info/', include('info.urls')),
    path('shop/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('news/', include('news_articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
