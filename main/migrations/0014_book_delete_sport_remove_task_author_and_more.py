# Generated by Django 4.0.2 on 2022-03-17 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_task_tasks_task_author_task_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='')),
                ('author', models.CharField(default='anonymous', max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('describe', models.TextField(default='DataFlair Django tutorials')),
            ],
        ),
        migrations.DeleteModel(
            name='sport',
        ),
        migrations.RemoveField(
            model_name='task',
            name='author',
        ),
        migrations.RemoveField(
            model_name='task',
            name='content',
        ),
        migrations.RemoveField(
            model_name='task',
            name='describe',
        ),
        migrations.RemoveField(
            model_name='task',
            name='email',
        ),
        migrations.RemoveField(
            model_name='task',
            name='picture',
        ),
        migrations.AddField(
            model_name='task',
            name='tasks',
            field=models.TextField(default=' ', max_length=100),
        ),
    ]
