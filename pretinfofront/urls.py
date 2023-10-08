from django.urls import path
from pretinfofront import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pretinfofront'

urlpatterns = [
    path('', views.index, name='index'),
]