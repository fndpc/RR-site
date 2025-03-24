from django.urls import path, include
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
path('', cache_page(600)(views.main)),
path('news/', include('news.urls')),
path('merch/', include('merch.urls')),
path('concerts/', include('concerts.urls')),
path('snippets/', include('snippets.urls')),
path('logout/', views.logout_user),
]