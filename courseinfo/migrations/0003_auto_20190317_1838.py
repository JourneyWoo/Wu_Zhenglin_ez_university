# Generated by Django 2.1.1 on 2019-03-17 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0002_auto_20190210_0915'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('semester', 'course', 'section_name')},
        ),
    ]
