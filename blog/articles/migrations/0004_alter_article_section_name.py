# Generated by Django 4.2 on 2023-04-03 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_article_section_article_section_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='section_name',
            field=models.CharField(choices=[('dn', 'Daily News'), ('sp', 'Sport'), ('cu', 'Culture'), ('mu', 'Music'), ('bu', 'Business')], default='', max_length=2),
        ),
    ]
