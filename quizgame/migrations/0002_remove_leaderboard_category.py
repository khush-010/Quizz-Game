# Generated by Django 5.0.6 on 2024-06-19 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizgame', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='category',
        ),
    ]