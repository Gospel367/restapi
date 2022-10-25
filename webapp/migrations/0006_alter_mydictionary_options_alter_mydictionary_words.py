# Generated by Django 4.0.2 on 2022-07-11 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_mydictionary_type_alter_mydictionary_words'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mydictionary',
            options={'ordering': ['words'], 'verbose_name': 'My English Dictionary', 'verbose_name_plural': 'My English Dictionary'},
        ),
        migrations.AlterField(
            model_name='mydictionary',
            name='words',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]