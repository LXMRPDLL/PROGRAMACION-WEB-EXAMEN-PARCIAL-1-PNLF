# Generated by Django 4.1.1 on 2022-09-19 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=64)),
                ('capacity', models.IntegerField()),
                ('location', models.CharField(max_length=32)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(default='generic-stadium', max_length=32)),
            ],
        ),
    ]