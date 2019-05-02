# Generated by Django 2.0.12 on 2019-05-02 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarningValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='预警值')),
                ('terminal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibition.TerminalInfo', verbose_name='终端名称')),
            ],
            options={
                'verbose_name': '终端预警值',
                'verbose_name_plural': '终端预警值',
            },
        ),
    ]
