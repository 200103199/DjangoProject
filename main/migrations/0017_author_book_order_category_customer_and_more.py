# Generated by Django 4.0.2 on 2022-04-29 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_description', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='describe',
        ),
        migrations.RemoveField(
            model_name='book',
            name='email',
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.book')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.book_order')),
            ],
        ),
        migrations.AddField(
            model_name='book_order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.customer'),
        ),
        migrations.CreateModel(
            name='Author_Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.author')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
    ]
