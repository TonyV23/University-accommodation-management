# Generated by Django 4.2.3 on 2023-12-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedroom',
            name='category',
            field=models.CharField(choices=[('HOMME', 'Male'), ('Femme', 'female')], max_length=10),
        ),
    ]