# Generated by Django 4.2.3 on 2023-12-19 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_application_status'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='application',
            name='unique_bedroom_application',
        ),
        migrations.AddConstraint(
            model_name='application',
            constraint=models.UniqueConstraint(fields=('matricule', 'student', 'status'), name='unique_bedroom_application'),
        ),
    ]
