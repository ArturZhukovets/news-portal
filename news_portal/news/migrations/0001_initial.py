# Generated by Django 4.0.3 on 2022-05-19 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('anons', models.CharField(default='', max_length=250, verbose_name='preview')),
                ('full_text', models.TextField()),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
