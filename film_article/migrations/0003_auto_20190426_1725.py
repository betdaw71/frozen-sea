# Generated by Django 2.2 on 2019-04-26 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('film_article', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='film_article.Category'),
        ),
        migrations.AddField(
            model_name='genre',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='film_article.Category'),
        ),
    ]
