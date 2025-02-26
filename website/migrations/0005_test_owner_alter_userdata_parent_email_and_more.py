# Generated by Django 5.1.3 on 2024-12-04 06:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_userdata_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tests_owner', to='website.userdata'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='parent_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='parent_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='phone_number',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='role',
            field=models.CharField(blank=True, choices=[('student', 'Student'), ('administrator', 'Administrator')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='roll_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='school_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
