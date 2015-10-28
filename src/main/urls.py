from django.conf.urls import url
from vanilla import ListView
from .models import Test
from .views import PassTestView

urlpatterns = [
    url(r'^$', ListView.as_view(model=Test), name='test-list'),
    url(r'^test_(?P<pk>\d+)/$', PassTestView.as_view(), name='test-pass'),
]

