# Generated by Django 4.1.1 on 2022-11-27 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_events_notice_socity_members_visitors_watchman_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='notice_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
