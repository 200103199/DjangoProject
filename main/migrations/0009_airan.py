# Generated by Django 4.0.2 on 2022-03-11 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_delete_kymyz'),
    ]

    operations = [
        migrations.CreateModel(
            name='airan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('airan', models.TextField(default=' ', max_length=100)),
            ],
        ),
    ]
