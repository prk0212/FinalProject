# Generated by Django 3.1.2 on 2021-04-20 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VIKIPI_CUSTOMER_PANEL', '0013_auto_20210420_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_details',
            name='employee_id',
        ),
    ]
