# Generated by Django 4.2 on 2023-04-03 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='section',
        ),
        migrations.AddField(
            model_name='article',
            name='section_name',
            field=models.CharField(choices=[('dn', 'Daily News'), ('sp', 'Sport'), ('cu', 'Culture'), ('mu', 'Music'), ('bu', 'Business')], default=('dn', 'Daily News'), max_length=2),
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]