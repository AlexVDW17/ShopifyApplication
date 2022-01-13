# Generated by Django 4.0.1 on 2022-01-13 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApi', '0004_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sku',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='inventoryApi.product'),
        ),
    ]