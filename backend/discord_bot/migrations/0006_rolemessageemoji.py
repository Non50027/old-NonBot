# Generated by Django 5.1.1 on 2024-12-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discord_bot', '0005_alter_livetwitch_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleMessageEmoji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guild', models.IntegerField()),
                ('role', models.IntegerField()),
                ('message', models.IntegerField()),
                ('emoji', models.IntegerField()),
            ],
        ),
    ]
