# Generated by Django 4.0.2 on 2022-07-11 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_alter_mydictionary_options_alter_mydictionary_words'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydictionary',
            name='words',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
