# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-20 17:33
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('billing', '0006_card_default'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(max_length=120)),
                ('paid', models.BooleanField(default=False)),
                ('refunded', models.BooleanField(default=False)),
                ('outcome', models.TextField(blank=True, null=True)),
                ('outcome_type', models.CharField(blank=True, max_length=120, null=True)),
                ('seller_message', models.CharField(blank=True, max_length=120, null=True)),
                ('risk_level', models.CharField(blank=True, max_length=120, null=True)),
                ('billing_profile',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile')),
            ],
        ),
    ]
