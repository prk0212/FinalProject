# Generated by Django 3.1.7 on 2021-05-05 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('VIKIPI_CUSTOMER_PANEL', '0018_auto_20210505_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date_of_order',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='ord_deliver_otp',
            field=models.IntegerField(default=7878),
        ),
        migrations.AddField(
            model_name='transaction',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.DeleteModel(
            name='order_details',
        ),
    ]
