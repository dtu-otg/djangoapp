# Generated by Django 3.1.7 on 2021-04-03 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_remove_inviteonly_otp_expires'),
    ]

    operations = [
        migrations.AddField(
            model_name='inviteonly',
            name='sender',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]