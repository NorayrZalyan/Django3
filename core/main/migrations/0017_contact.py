# Generated by Django 5.1.2 on 2024-10-20 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_a_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bgimg', models.ImageField(upload_to='media', verbose_name='bg img')),
                ('adress', models.CharField(max_length=50, verbose_name='adress')),
                ('email', models.CharField(max_length=50, verbose_name='email')),
                ('tel', models.CharField(max_length=50, verbose_name='tel')),
                ('facebook', models.CharField(max_length=50, verbose_name='facebook')),
                ('instagram', models.CharField(max_length=50, verbose_name='instagram')),
            ],
        ),
    ]
