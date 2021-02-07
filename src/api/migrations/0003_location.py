# Generated by Django 3.1.6 on 2021-02-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210207_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150)),
                ('neighborhood', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('nation', models.CharField(max_length=70)),
                ('lat', models.IntegerField(blank=True, null=True)),
                ('lon', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
