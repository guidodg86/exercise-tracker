# Generated by Django 4.0.1 on 2022-01-24 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('duration', models.IntegerField(default=1)),
                ('date_exercise', models.DateField()),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Exercises', to='mainapp.user')),
            ],
        ),
    ]
