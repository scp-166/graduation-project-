# Generated by Django 2.0.12 on 2019-05-01 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TerminalCategory',
            fields=[
                ('category_id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, verbose_name='设备种类id')),
                ('category_name', models.CharField(max_length=20, verbose_name='设备种类名称')),
            ],
            options={
                'verbose_name': '终端设备种类',
                'verbose_name_plural': '终端设备种类',
            },
        ),
        migrations.CreateModel(
            name='TerminalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FloatField(default=0.0, verbose_name='终端数据')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '终端数据',
                'verbose_name_plural': '终端数据',
            },
        ),
        migrations.CreateModel(
            name='TerminalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terminal_id', models.PositiveSmallIntegerField(verbose_name='终端id')),
                ('terminal_name', models.CharField(max_length=20, verbose_name='终端名称')),
                ('status', models.BooleanField(default=False, verbose_name='终端状态')),
                ('terminal_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibition.TerminalCategory', verbose_name='设备种类id')),
            ],
            options={
                'verbose_name': '终端信息',
                'verbose_name_plural': '终端信息',
            },
        ),
        migrations.AddField(
            model_name='terminaldata',
            name='terminal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibition.TerminalInfo', verbose_name='终端id'),
        ),
        migrations.AlterUniqueTogether(
            name='terminalinfo',
            unique_together={('terminal_category', 'terminal_id')},
        ),
    ]
