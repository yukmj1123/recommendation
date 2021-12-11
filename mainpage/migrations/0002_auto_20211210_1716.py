# Generated by Django 3.2.8 on 2021-12-10 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jeonbuk',
            fields=[
                ('place', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('y2018', models.IntegerField(blank=True, null=True)),
                ('y2019', models.IntegerField(blank=True, null=True)),
                ('y2020', models.IntegerField(blank=True, null=True)),
                ('y2021', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'jeonbuk',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainpageBusan',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('place', models.CharField(max_length=30)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('subject', models.CharField(max_length=30)),
                ('total', models.IntegerField()),
                ('y2018', models.IntegerField()),
                ('y2019', models.IntegerField()),
                ('y2020', models.IntegerField()),
                ('y2021', models.IntegerField()),
            ],
            options={
                'db_table': 'mainpage_busan',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='busan',
        ),
    ]