# Generated by Django 3.2.19 on 2023-06-25 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymaps', '0012_alter_voters_with_latlon_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voterslatlon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward', models.IntegerField()),
                ('pct', models.CharField(max_length=1)),
                ('voter_id', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('title', models.CharField(blank=True, max_length=10)),
                ('street_number', models.CharField(max_length=100)),
                ('street_name', models.CharField(max_length=100)),
                ('apt_number', models.CharField(blank=True, max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
                ('party_affiliation', models.CharField(blank=True, max_length=100)),
                ('date_of_birth', models.CharField(blank=True, max_length=255)),
                ('voter_status', models.CharField(max_length=1)),
                ('longitude', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('full_address', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='voters_with_latlon',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]