# Generated by Django 4.1.1 on 2022-11-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_mst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=25)),
                ('product_price', models.IntegerField()),
                ('Product_image', models.FileField(default='a.png', upload_to=None)),
            ],
        ),
    ]
