# Generated by Django 5.1.1 on 2024-10-03 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discord_bot', '0007_alter_rankchat_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='livetwitch',
            name='guild',
            field=models.CharField(default=482720923431206932, max_length=50),
            preserve_default=False,
        ),
    ]
