# Generated by Django 4.2.7 on 2023-12-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCardDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.BigIntegerField()),
                ('expirely_date', models.DateField()),
                ('CVV', models.CharField(max_length=255)),
            ],
        ),
    ]
