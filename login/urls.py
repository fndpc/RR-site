from django.urls import path, include
from . import views
from . views import LoginFormView

urlpatterns = [
path('', LoginFormView.as_view()),
]