from django.conf.urls import url

from . import views

app_name = 'accounts'
urlpatterns = [
    url('signup/', views.SignUp.as_view(), name='signup'),
]