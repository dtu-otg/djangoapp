# Generated by Django 3.2.6 on 2021-08-11 11:14

from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210322_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default='events/default.jpeg', upload_to=events.models.upload_to, verbose_name='Image'),
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]