# Generated by Django 3.0.4 on 2020-04-27 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.TextField(max_length=200)),
                ('pub_date', models.TextField(max_length=200)),
                ('body', models.TextField(max_length=200)),
            ],
        ),
    ]