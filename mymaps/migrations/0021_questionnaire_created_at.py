# Generated by Django 3.2.19 on 2023-07-05 09:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mymaps', '0020_auto_20230705_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
