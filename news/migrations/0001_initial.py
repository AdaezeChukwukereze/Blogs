# Generated by Django 4.2.3 on 2023-07-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateField()),
                ('reporter', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
    ]
