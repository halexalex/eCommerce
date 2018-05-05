from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

from accounts.views import GuestRegisterView, LoginView, RegisterView
from addresses.views import (checkout_address_create_view,
                             checkout_address_reuse_view,
                             AddressCreateView,
                             AddressListView,
                             AddressUpdateView,
                             )
from billing.views import payment_method_create_view, payment_method_view
from carts.views import cart_detail_api_view
from marketing.views import MailChimpWebhookView, MarketingPreferenceUpdateView
from orders.views import LibraryView

from .views import about_page, contact_page, home_page

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^about/$', about_page, name='about'),
    url(r'^accounts/$', RedirectView.as_view(url='/account')),
    url(r'^account/', include('accounts.urls', namespace='account')),
    url(r'^accounts/', include('accounts.passwords.urls')),
    url(r'^address/$', RedirectView.as_view(url='/addresses')),
    url(r'^addresses/$', AddressListView.as_view(), name='addresses'),
    url(r'^addresses/create/$', AddressCreateView.as_view(), name='address-create'),
    url(r'^addresses/(?P<pk>\d+)/$', AddressUpdateView.as_view(), name='address-update'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name='checkout_address_reuse'),
    url(r'^register/guest/$', GuestRegisterView.as_view(), name='guest_register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/cart/$', cart_detail_api_view, name='api-cart'),
    url(r'^cart/', include('carts.urls', namespace='cart')),
    url(r'^billing/payment-method/$', payment_method_view, name='billing-payment-method'),
    url(r'^billing/payment-method/create/$', payment_method_create_view, name='billing-payment-method-endpoint'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^library/$', LibraryView.as_view(), name='library'),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^products/', include('products.urls', namespace='products')),
    url(r'^search/', include('search.urls', namespace='search')),
    url(r'^settings/$', RedirectView.as_view(url='/account')),
    url(r'^settings/email/$', MarketingPreferenceUpdateView.as_view(), name='marketing-pref'),
    url(r'^webhooks/mailchimp/$', MailChimpWebhookView.as_view(), name='webhooks-mailchimp'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



