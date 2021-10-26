# Generated by Django 3.2.8 on 2021-10-26 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Product ID')),
                ('product_name', models.CharField(max_length=120)),
                ('product_price', models.IntegerField()),
                ('before_discount_price', models.FloatField()),
                ('product_description', models.TextField()),
                ('product_pic', models.ImageField(upload_to='product-images/')),
            ],
        ),
    ]
