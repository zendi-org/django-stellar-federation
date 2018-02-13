from .views import federation
from django.conf.urls import url

urlpatterns = [
    url(r'^$', federation, name='federation')
]
