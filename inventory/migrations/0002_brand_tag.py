# Generated by Django 5.0.3 on 2024-04-03 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='tag',
            field=models.ManyToManyField(to='inventory.tag'),
        ),
    ]
