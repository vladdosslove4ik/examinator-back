# Generated by Django 4.0.4 on 2023-01-18 13:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moderator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nickname', models.CharField(max_length=30)),
                ('imie', models.CharField(max_length=254)),
                ('nazwisko', models.CharField(max_length=254)),
                ('haslo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField(default=django.utils.timezone.now)),
                ('creditCardNumber', models.CharField(max_length=30)),
                ('creditCardExpirationDate', models.DateField()),
                ('creditCardCode', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254)),
                ('nickname', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('imie', models.CharField(max_length=254)),
                ('nazwisko', models.CharField(max_length=254)),
                ('haslo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.user')),
                ('subscription', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.subscription')),
            ],
            bases=('base.user',),
        ),
    ]
