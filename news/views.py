from django.shortcuts import render
from django.http import HttpResponse
from . models import News
from django.views.generic import ListView
# Create your views here.


def allnews(request):
    news1 = News.objects.all()
    news = {'news': news1}
    return render(request, 'news/news.html', news)



class GetNews(ListView):
    model = News
    context_object_name = 'all_news'
    template_name = 'news/news.html'