from django.conf.urls import url

from .views import BlogPostRUDView, BlogPostAPIView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogPostRUDView.as_view(), name='post-rud'),
    url(r'^$', BlogPostAPIView.as_view(), name='post-create')
]