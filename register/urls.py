from django.urls import path
from . import views
from . views import RegisterFormView



urlpatterns = [
path('', RegisterFormView.as_view()),
]