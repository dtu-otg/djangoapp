# Generated by Django 3.1.7 on 2021-03-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='time_code',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
