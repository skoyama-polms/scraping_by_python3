from django.urls import path

from . import views

app_name = 'scraping'
urlpatterns = [
    path('', views.index, name='index'),
    path('doScraping/', views.do_scraping, name='doScraping'),
]
