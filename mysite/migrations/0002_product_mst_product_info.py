# Generated by Django 4.1.1 on 2022-11-18 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_mst',
            name='product_info',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
