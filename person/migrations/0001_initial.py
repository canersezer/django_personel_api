# Generated by Django 5.0.4 on 2024-04-08 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('title', models.CharField(choices=[('Team_Lead', 'TL'), ('Mid_Lead', 'ML'), ('Junior', 'JR')], max_length=10)),
                ('gender', models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Order', 'O')], max_length=10)),
                ('salary', models.PositiveIntegerField()),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('departman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.departman')),
            ],
        ),
    ]