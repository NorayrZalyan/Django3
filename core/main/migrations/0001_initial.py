# Generated by Django 5.1.2 on 2024-10-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p', models.CharField(max_length=75, verbose_name='title')),
                ('text', models.TextField(verbose_name='text')),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_img', models.ImageField(upload_to='media', verbose_name='logo')),
                ('about_the_page', models.CharField(max_length=150, verbose_name='about the page')),
                ('img', models.ImageField(upload_to='media', verbose_name='page img')),
            ],
        ),
    ]
