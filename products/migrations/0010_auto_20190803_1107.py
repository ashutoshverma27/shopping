# Generated by Django 2.1.3 on 2019-08-03 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20190803_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_on_amazon',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
