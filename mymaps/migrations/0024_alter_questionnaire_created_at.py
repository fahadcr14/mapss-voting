# Generated by Django 3.2.19 on 2023-07-07 05:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mymaps', '0023_alter_questionnaire_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
