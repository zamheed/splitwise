# Generated by Django 2.1.3 on 2018-12-15 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181215_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenditure',
            name='name',
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Register'),
        ),
    ]
