# Generated by Django 3.1.7 on 2021-05-05 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIKIPI_ADMIN_PANEL', '0013_product_shop_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='retailer',
            name='otp_status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]
