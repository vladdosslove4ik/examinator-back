# Generated by Django 4.0.4 on 2023-01-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_blocked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessuser',
            name='creditCardExpirationDate',
            field=models.CharField(max_length=5),
        ),
    ]