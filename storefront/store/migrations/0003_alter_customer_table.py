# Generated by Django 4.1.5 on 2023-01-12 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_slug'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='store_customers',
        ),
    ]
