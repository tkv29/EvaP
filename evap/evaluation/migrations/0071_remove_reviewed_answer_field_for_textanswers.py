# Generated by Django 2.0.5 on 2018-06-05 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0070_add_answer_field_for_textanswer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textanswer',
            name='reviewed_answer',
        ),
        migrations.AlterField(
            model_name='textanswer',
            name='answer',
            field=models.TextField(verbose_name='answer'),
        ),
    ]
