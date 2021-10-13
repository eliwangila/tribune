
from django.conf.urls import include, url
from django.contrib.auth import views
from django.contrib import admin


urlpatterns = [
    url('^admin/', admin.site.urls),
    url('', include('news.urls')),
    url('^accounts/', include('registration.backends.simple.urls')),
    url('^logout/$', views.LogoutView.as_view(), {"next_page": '/'}),
    url('^tinymce/', include('tinymce.urls')),
]