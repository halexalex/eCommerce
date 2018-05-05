from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import DetailView, ListView

from billing.models import BillingProfile
from .models import Order, ProductPurchase


class OrderListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Order.objects.by_request(self.request).exclude_created_status()


class OrderDetailView(LoginRequiredMixin, DetailView):

    def get_object(self, queryset=None):
        qs = Order.objects.by_request(
            self.request
        ).filter(
            order_id=self.kwargs.get('order_id')
        )
        if qs.count() == 1:
            return qs.first()
        raise Http404

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request=self.request)
        context['billing_profile'] = billing_profile
        return context


class LibraryView(LoginRequiredMixin, ListView):
    template_name = 'orders/library.html'

    def get_queryset(self):
        return ProductPurchase.objects.products_by_request(self.request)
