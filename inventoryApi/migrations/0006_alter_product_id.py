# Generated by Django 4.0.1 on 2022-01-13 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApi', '0005_alter_item_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]