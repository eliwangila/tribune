# from django.urls import path,include
from django.conf.urls import include, url
from django.contrib import admin
from news import views

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('', include('news.urls'))
]