# Generated by Django 5.0.6 on 2024-07-24 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='名'),
        ),
    ]