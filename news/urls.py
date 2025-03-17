from django.urls import path, include
from . import views
from . views import GetNews

urlpatterns = [
path('', GetNews.as_view()),
]