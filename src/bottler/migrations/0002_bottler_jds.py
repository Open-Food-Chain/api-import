# Generated by Django 3.1 on 2020-08-25 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottler',
            name='jds',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]