# Generated by Django 2.1.5 on 2024-04-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20240322_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='current_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
