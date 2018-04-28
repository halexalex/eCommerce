from django.core.urlresolvers import reverse
from django.db import models

from billing.models import BillingProfile

ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping')
)


class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile)
    name = models.CharField(max_length=120, null=True, blank=True, help_text='Shipping to? Who is it for?')
    nickname = models.CharField(max_length=120, null=True, blank=True, help_text='Internal Reference Nickname')
    address_type = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    address_line_1 = models.CharField(max_length=120)
    address_line_2 = models.CharField(max_length=120, null=True, blank=True)
    country = models.CharField(max_length=120, default='Russia')
    city = models.CharField(max_length=120)
    region = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)

    def __str__(self):
        if self.nickname:
            return str(self.nickname)
        return str(self.billing_profile)

    def get_absolute_url(self):
        return reverse('address-update', kwargs={'pk': self.pk})

    def get_short_address(self):
        for_name = self.name
        if self.nickname:
            for_name = f"{self.nickname} | {for_name}"
        return "{for_name} {line1}, {city}".format(
            for_name=for_name or '',
            line1=self.address_line_1,
            city=self.city
        )

    def get_address(self):
        return "{for_name}\n{line1}\n{line2}\n{city}\n{region}, {postal}\n{country}".format(
            for_name=self.name or "",
            line1=self.address_line_1,
            line2=self.address_line_2 or "",
            city=self.city,
            region=self.region,
            postal=self.postal_code,
            country=self.country
        )
