# Generated by Django 4.2.1 on 2023-05-31 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0003_auto_puissance'),
    ]

    operations = [
        migrations.AddField(
            model_name='marque',
            name='createur',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
