# Generated by Django 4.0.4 on 2023-01-19 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_businessuser_creditcardcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(editable=False, max_length=30, primary_key=True, serialize=False),
        ),
    ]
