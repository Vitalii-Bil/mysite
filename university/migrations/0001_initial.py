# Generated by Django 3.1.4 on 2021-01-13 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('date_of_found', models.DateField(blank=True, null=True, verbose_name='date of foundation')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('lecturer', models.ManyToManyField(to='university.Lecturer', verbose_name='lecturer')),
                ('university', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='university.university')),
            ],
        ),
        migrations.CreateModel(
            name='Rector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('university', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='university.university')),
            ],
        ),
        migrations.AddField(
            model_name='lecturer',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='university.university'),
        ),
    ]
