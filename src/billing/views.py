from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.utils.http import is_safe_url

import stripe

from .models import BillingProfile, Card

stripe.api_key = settings.STRIPE_SECRET_KEY
STRIPE_PUB_KEY = settings.STRIPE_PUB_KEY


def payment_method_view(request):
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if not billing_profile:
        return redirect('/cart')

    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY, "next_url": next_url})


def payment_method_create_view(request):
    if request.method == "POST" and request.is_ajax():
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            return HttpResponse({"message": "Cannot find this user"}, status_code=404)

        token = request.POST.get("token")
        if token is not None:
            customer = stripe.Customer.retrieve(billing_profile.customer_id)
            card_response = customer.sources.create(source=token)
            new_card_object = Card.objects.add_new(billing_profile, card_response)
            print(new_card_object)
            return JsonResponse({"message": "Success! Your card was added."})

    return HttpResponse("error", status_code=401)
