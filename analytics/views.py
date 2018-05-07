from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class SalesView(LoginRequiredMixin, TemplateView):
    template_name = 'analytics/sales.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return render(self.request, "400.html", {})
        return super(SalesView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super(SalesView, self).get_context_data(**kwargs)
