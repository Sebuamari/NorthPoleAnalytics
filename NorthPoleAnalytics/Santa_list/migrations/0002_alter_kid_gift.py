# Generated by Django 5.1.4 on 2024-12-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Santa_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='gift',
            field=models.CharField(max_length=20),
        ),
    ]