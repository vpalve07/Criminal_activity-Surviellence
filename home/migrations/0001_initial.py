# Generated by Django 3.2.5 on 2021-09-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Criminal',
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
            name='ID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Officers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=122, null=True)),
                ('name2', models.CharField(max_length=122, null=True)),
                ('email1', models.CharField(max_length=122, null=True)),
                ('password1', models.CharField(max_length=12, null=True)),
                ('contact1', models.IntegerField(null=True)),
                ('rank1', models.CharField(max_length=122, null=True)),
                ('uniq1', models.IntegerField(null=True)),
                ('address01', models.TextField(null=True)),
                ('address02', models.TextField(null=True)),
                ('city1', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name11', models.CharField(max_length=122, null=True)),
                ('name22', models.CharField(max_length=122, null=True)),
                ('email11', models.CharField(max_length=122, null=True)),
                ('password11', models.CharField(max_length=12, null=True)),
                ('contact11', models.IntegerField(null=True)),
                ('pro11', models.CharField(max_length=122, null=True)),
                ('uniq11', models.IntegerField(null=True)),
                ('address11', models.TextField(null=True)),
                ('address22', models.TextField(null=True)),
                ('city11', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=122, null=True)),
                ('lname', models.CharField(max_length=122, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('city', models.CharField(max_length=122, null=True)),
                ('state', models.CharField(max_length=122, null=True)),
                ('zip', models.IntegerField(max_length=122, null=True)),
                ('complaint', models.TextField(max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Search_Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ufname', models.CharField(max_length=122, null=True)),
                ('ulname', models.CharField(max_length=122, null=True)),
                ('username', models.EmailField(max_length=122, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('city', models.CharField(max_length=122, null=True)),
                ('cfname', models.CharField(max_length=122, null=True)),
                ('clname', models.CharField(max_length=122, null=True)),
                ('reason', models.CharField(max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122, null=True)),
                ('password', models.CharField(max_length=12, null=True)),
                ('address', models.TextField(null=True)),
                ('address2', models.TextField(null=True)),
                ('city', models.TextField(null=True)),
                ('zip', models.IntegerField(null=True)),
            ],
        ),
    ]
