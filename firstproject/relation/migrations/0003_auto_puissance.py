# Generated by Django 4.2.1 on 2023-05-31 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0002_marque_pays'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='puissance',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
