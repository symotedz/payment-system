# Generated by Django 4.2.7 on 2023-12-15 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MpesaExpress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.PositiveBigIntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.PositiveBigIntegerField()),
                ('is_confirmed', models.BooleanField()),
            ],
        ),
    ]