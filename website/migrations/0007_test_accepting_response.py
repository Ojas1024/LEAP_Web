# Generated by Django 5.1.3 on 2024-12-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_question_visible_test_result_released'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='accepting_response',
            field=models.BooleanField(default=True),
        ),
    ]
