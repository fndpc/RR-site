from django.urls import path, include
from . import views

urlpatterns = [
path('', views.main),
path('news/', include('news.urls')),
path('merch/', include('merch.urls')),
path('concerts/', include('concerts.urls')),
path('snippets/', include('snippets.urls')),
path('logout/', views.logout_user),
]