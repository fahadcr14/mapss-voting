# Generated by Django 3.2.19 on 2023-06-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymaps', '0006_voters_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='voters_list',
            name='full_address',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]