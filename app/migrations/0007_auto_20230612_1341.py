# Generated by Django 2.2.28 on 2023-06-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20230612_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clr',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='clr',
            name='customer_type',
        ),
        migrations.AddField(
            model_name='clr',
            name='CUSTOMER_NAME',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clr',
            name='CUSTOMER_TYPE',
            field=models.CharField(max_length=255, null=True),
        ),
    ]