# Generated by Django 3.1.4 on 2021-04-10 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('VIKIPI_ADMIN_PANEL', '0012_auto_20210410_2246'),
        ('VIKIPI_CUSTOMER_PANEL', '0008_auto_20210410_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('phnumber', models.IntegerField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(max_length=100)),
                ('view', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('otp', models.IntegerField(default=4567)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_CUSTOMER_PANEL.customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_ADMIN_PANEL.product')),
            ],
        ),
        migrations.CreateModel(
            name='product_review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=500)),
                ('view', models.BooleanField(default=False)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_CUSTOMER_PANEL.customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_ADMIN_PANEL.product')),
            ],
        ),
        migrations.CreateModel(
            name='product_cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, max_length=3)),
                ('date_of_added', models.DateTimeField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_CUSTOMER_PANEL.customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_ADMIN_PANEL.product')),
            ],
        ),
        migrations.CreateModel(
            name='order_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=20)),
                ('date_of_order', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Panding', max_length=50)),
                ('date_of_delivered', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=1, max_length=3)),
                ('total_amount', models.IntegerField(max_length=10)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_CUSTOMER_PANEL.customer')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_ADMIN_PANEL.employee')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_ADMIN_PANEL.product')),
                ('retailer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_ADMIN_PANEL.retailer')),
            ],
        ),
        migrations.CreateModel(
            name='customer_FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall_experience', models.CharField(max_length=20)),
                ('timely_response', models.CharField(max_length=30)),
                ('our_support', models.CharField(max_length=30)),
                ('overall_setisfaction', models.CharField(max_length=30)),
                ('view', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_CUSTOMER_PANEL.customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_CUSTOMER_PANEL.user'),
        ),
    ]