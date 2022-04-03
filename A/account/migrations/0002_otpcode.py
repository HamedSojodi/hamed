# Generated by Django 4.0.3 on 2022-04-01 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtPCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('code', models.PositiveSmallIntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
