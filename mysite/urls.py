from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
    url('', TemplateView.as_view(template_name='home.html'), name='home'),
]
