# Generated by Django 2.2.6 on 2019-10-23 13:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillableItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('name', models.CharField(max_length=60)),
                ('financial_consumption_amount', models.DecimalField(decimal_places=10, default=0, max_digits=15)),
                ('account_status', models.CharField(choices=[('TRIAL', 'Trial'), ('PREMIUM', 'Premium')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('billable_items', models.ManyToManyField(to='backend.BillableItem')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_date', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pricing_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('price', models.DecimalField(decimal_places=10, max_digits=15)),
                ('account_status', models.CharField(choices=[('TRIAL', 'Trial'), ('PREMIUM', 'Premium')], max_length=20)),
                ('billable_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pricings', to='backend.BillableItem')),
            ],
        ),
    ]