# Generated by Django 4.1.1 on 2022-11-28 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_alter_notice_notice_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socity_members',
            old_name='Product_image',
            new_name='pic',
        ),
    ]