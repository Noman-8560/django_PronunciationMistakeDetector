# Generated by Django 3.2 on 2023-10-09 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quickstart', '0002_auto_20231009_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recording',
            name='correct_pronunciation',
        ),
        migrations.RemoveField(
            model_name='recording',
            name='word',
        ),
        migrations.AddField(
            model_name='recording',
            name='audio_data',
            field=models.BinaryField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recording',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recording',
            name='user',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]