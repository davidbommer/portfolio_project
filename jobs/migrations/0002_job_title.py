# Generated by Django 3.0.4 on 2020-05-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='', max_length=250),
        ),
    ]