# Generated by Django 2.1.4 on 2018-12-25 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News_model_out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('content', models.TextField()),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='News_model_total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('content', models.TextField()),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
    ]
