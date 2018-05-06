from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.views.generic import DetailView, ListView, View

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


class VerifyOwnership(View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            data = request.GET
            product_id = data.get('product_id', None)
            if product_id is not None:
                product_id = int(product_id)
                ownership_ids = ProductPurchase.objects.products_by_id(request)
                if product_id in ownership_ids:
                    return JsonResponse({'owner': True})
            return JsonResponse({'owner': False})
        raise Http404
