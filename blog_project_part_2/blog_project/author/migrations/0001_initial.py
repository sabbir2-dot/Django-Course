# Generated by Django 5.1.2 on 2024-11-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('bio', models.TextField()),
                ('phone_no', models.CharField(max_length=12)),
            ],
        ),
    ]
