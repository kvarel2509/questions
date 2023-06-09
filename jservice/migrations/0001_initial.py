# Generated by Django 4.2.1 on 2023-05-29 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.TextField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('loaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'questions',
                'indexes': [models.Index(fields=['-loaded_at'], name='questions_loaded__72c61d_idx')],
            },
        ),
    ]
