from django.conf.urls import url

from .views import ProductDetailSlugView, ProductListView

urlpatterns = [
    url(r'^products/$', ProductListView.as_view()),
    url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
]
