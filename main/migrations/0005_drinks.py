# Generated by Django 4.0.2 on 2022-03-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_sport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drinks', models.CharField(max_length=50)),
            ],
        ),
    ]