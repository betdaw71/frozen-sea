# Generated by Django 2.2.1 on 2019-05-08 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('film_article', '0006_auto_20190507_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Star_article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film_article.Article')),
            ],
        ),
    ]