# Generated by Django 5.1.2 on 2024-10-19 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='choice_field',
            field=models.CharField(choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3')], default='option1', max_length=20),
        ),
    ]
