# Generated by Django 5.1.2 on 2024-10-20 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='A_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('img', models.ImageField(upload_to='media', verbose_name='img')),
                ('link', models.CharField(max_length=50, verbose_name='link')),
            ],
        ),
    ]
