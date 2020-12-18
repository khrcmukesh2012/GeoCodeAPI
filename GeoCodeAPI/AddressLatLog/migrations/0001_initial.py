# Generated by Django 3.1.4 on 2020-12-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=50, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('log', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
