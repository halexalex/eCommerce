# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-19 08:03
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('billing', '0003_auto_20180118_1654'),
        ('orders', '0002_auto_20180110_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='billing_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='billing.BillingProfile'),
        ),
    ]