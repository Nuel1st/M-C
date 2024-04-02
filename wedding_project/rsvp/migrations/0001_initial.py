# Generated by Django 4.1.4 on 2024-04-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('attending', models.BooleanField(default=False)),
                ('guests', models.IntegerField(default=1)),
            ],
        ),
    ]