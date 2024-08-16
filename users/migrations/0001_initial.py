# Generated by Django 5.0 on 2024-08-03 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('slogan', models.CharField(max_length=127)),
                ('description', models.CharField(max_length=2047)),
                ('members_count', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=50)),
                ('registration_date', models.DateField()),
                ('level', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='lieder',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='lieder_group', to='users.player'),
        ),
    ]