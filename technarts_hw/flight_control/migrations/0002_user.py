# Generated by Django 4.2.3 on 2023-07-18 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]