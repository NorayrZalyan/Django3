# Generated by Django 5.1.2 on 2024-10-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='about_the_page',
            field=models.CharField(max_length=150, verbose_name=' about the page'),
        ),
        migrations.AlterField(
            model_name='header',
            name='company_name',
            field=models.CharField(max_length=30, verbose_name='company name'),
        ),
    ]
