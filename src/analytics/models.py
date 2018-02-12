from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

User = settings.AUTH_USER_MODEL


class ObjectViewed(models.Model):
    user           = models.ForeignKey(User, blank=True,  null=True)  # User instance
    ip_address     = models.CharField(max_length=220, blank=True, null=True)  # IP Field
    content_type   = models.ForeignKey(ContentType)  # User, Product, Order, Cart, Address
    object_id      = models.PositiveIntegerField()   # User id, Product id, Order id
    content_object = GenericForeignKey('content_type', 'object_id')  # Product instance
    timestamp      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.content_object} viewed on {self.timestamp}'

    class Meta:
        ordering = ['-timestamp']  # most recent saved show up first
        verbose_name = 'Object viewed'
        verbose_name_plural = 'Objects viewed'
