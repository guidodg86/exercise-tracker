# Generated by Django 4.0.1 on 2022-01-25 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='_id',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
    ]
