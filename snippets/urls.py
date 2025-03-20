from django.urls import path, include
from . views import SnippetsView, SnippetsAddView


urlpatterns = [
path('', SnippetsView.as_view(), name='snipet-list'),
path('add/', SnippetsAddView.as_view()),
]