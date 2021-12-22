# Generated by Django 3.1.7 on 2021-12-21 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0018_auto_20211017_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AnswerName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crimeName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CAQS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crime.answer')),
                ('crime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crime.crime')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crime.question')),
                ('suspect', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crime.suspect')),
            ],
        ),
    ]
