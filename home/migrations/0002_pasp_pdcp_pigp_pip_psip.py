# Generated by Django 3.2.5 on 2021-10-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PASP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=122, null=True)),
                ('lname', models.CharField(max_length=122, null=True)),
                ('age', models.IntegerField(max_length=3, null=True)),
                ('charges', models.CharField(max_length=122, null=True)),
                ('city', models.CharField(max_length=122, null=True)),
                ('zip', models.IntegerField(max_length=122, null=True)),
                ('duration', models.CharField(max_length=122, null=True)),
                ('uniq1', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=122, null=True)),
                ('image', models.ImageField(upload_to='static/images')),
                ('status', models.CharField(max_length=122, null=True)),
                ('fname1', models.CharField(max_length=122, null=True)),
                ('lname1', models.CharField(max_length=122, null=True)),
                ('age1', models.IntegerField(null=True)),
                ('rank', models.CharField(max_length=122, null=True)),
                ('phone', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PDCP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=122, null=True)),
                ('lname', models.CharField(max_length=122, null=True)),
                ('age', models.IntegerField(max_length=3, null=True)),
                ('charges', models.CharField(max_length=122, null=True)),
                ('city', models.CharField(max_length=122, null=True)),
                ('zip', models.IntegerField(max_length=122, null=True)),
                ('duration', models.CharField(max_length=122, null=True)),
                ('uniq1', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=122, null=True)),
                ('image', models.ImageField(upload_to='static/images')),
                ('status', models.CharField(max_length=122, null=True)),
                ('fname1', models.CharField(max_length=122, null=True)),
                ('lname1', models.CharField(max_length=122, null=True)),
                ('age1', models.IntegerField(null=True)),
                ('rank', models.CharField(max_length=122, null=True)),
                ('phone', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PIGP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=122, null=True)),
                ('lname', models.CharField(max_length=122, null=True)),
                ('age', models.IntegerField(max_length=3, null=True)),
                ('charges', models.CharField(max_length=122, null=True)),
                ('city', models.CharField(max_length=122, null=True)),
                ('zip', models.IntegerField(max_length=122, null=True)),
                ('duration', models.CharField(max_length=122, null=True)),
                ('uniq1', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=122, null=True)),
                ('image', models.ImageField(upload_to='static/images')),
                ('status', models.CharField(max_length=122, null=True)),
                ('fname1', models.CharField(max_length=122, null=True)),
                ('lname1', models.CharField(max_length=122, null=True)),
                ('age1', models.IntegerField(null=True)),
                ('rank', models.CharField(max_length=122, null=True)),
                ('phone', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=122, null=True)),
                ('lname', models.CharField(max_length=122, null=True)),
                ('age', models.IntegerField(max_length=3, null=True)),
                ('charges', models.CharField(max_length=122, null=True)),
                ('city', models.CharField(max_length=122, null=True)),
                ('zip', models.IntegerField(max_length=122, null=True)),
                ('duration', models.CharField(max_length=122, null=True)),
                ('uniq1', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=122, null=True)),
                ('image', models.ImageField(upload_to='static/images')),
                ('status', models.CharField(max_length=122, null=True)),
                ('fname1', models.CharField(max_length=122, null=True)),
                ('lname1', models.CharField(max_length=122, null=True)),
                ('age1', models.IntegerField(null=True)),
                ('rank', models.CharField(max_length=122, null=True)),
                ('phone', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PSIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=122, null=True)),
                ('lname', models.CharField(max_length=122, null=True)),
                ('age', models.IntegerField(max_length=3, null=True)),
                ('charges', models.CharField(max_length=122, null=True)),
                ('city', models.CharField(max_length=122, null=True)),
                ('zip', models.IntegerField(max_length=122, null=True)),
                ('duration', models.CharField(max_length=122, null=True)),
                ('uniq1', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=122, null=True)),
                ('image', models.ImageField(upload_to='static/images')),
                ('status', models.CharField(max_length=122, null=True)),
                ('fname1', models.CharField(max_length=122, null=True)),
                ('lname1', models.CharField(max_length=122, null=True)),
                ('age1', models.IntegerField(null=True)),
                ('rank', models.CharField(max_length=122, null=True)),
                ('phone', models.IntegerField(null=True)),
            ],
        ),
    ]
