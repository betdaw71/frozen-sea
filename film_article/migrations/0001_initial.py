# Generated by Django 2.2 on 2019-04-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('original_name', models.CharField(default='?', max_length=500)),
                ('body', models.TextField()),
                ('rating', models.BigIntegerField()),
                ('iframe', models.TextField()),
                ('trailer', models.TextField(default='')),
                ('img', models.ImageField(default='media/default.jpg', upload_to='media/')),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('data', models.BigIntegerField(default=2019)),
                ('length', models.BigIntegerField(default=0)),
                ('actor', models.TextField(default='?')),
                ('director', models.CharField(default='?', max_length=255)),
                ('country', models.TextField(default='?')),
                ('quolity', models.CharField(default='?', max_length=255)),
                ('translation', models.CharField(default='?', max_length=255)),
                ('ganre', models.ManyToManyField(to='film_article.Genre')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
