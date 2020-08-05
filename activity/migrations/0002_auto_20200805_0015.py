# Generated by Django 3.0.8 on 2020-08-04 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period',
            name='member_id',
        ),
        migrations.AddField(
            model_name='period',
            name='member',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='activity.Member'),
        ),
    ]