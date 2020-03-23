# Generated by Django 2.2 on 2020-03-22 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_extendeduser_last_fetched'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeduser',
            name='last_fetched',
        ),
        migrations.RemoveField(
            model_name='extendeduser',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='extendeduser',
            name='longitude',
        ),
        migrations.CreateModel(
            name='locationDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('last_fetched', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]