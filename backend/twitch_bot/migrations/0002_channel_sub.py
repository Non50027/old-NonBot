# Generated by Django 5.1.1 on 2024-12-05 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discord_bot', '0002_remove_livetwitch_twitch_channel'),
        ('twitch_bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='sub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='twitch_channel', to='discord_bot.livetwitch'),
        ),
    ]
