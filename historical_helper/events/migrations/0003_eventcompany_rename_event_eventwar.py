# Generated by Django 5.1.6 on 2025-03-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Event',
            new_name='EventWar',
        ),
    ]
