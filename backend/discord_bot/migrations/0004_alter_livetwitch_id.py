# Generated by Django 5.1.1 on 2024-12-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discord_bot', '0003_alter_livetwitch_channel_alter_livetwitch_guild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livetwitch',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
