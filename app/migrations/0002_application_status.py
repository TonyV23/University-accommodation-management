# Generated by Django 4.2.3 on 2023-12-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
