# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-27 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('datatype', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('field', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('label', models.CharField(blank=True, default='', max_length=256)),
                ('hint', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('form', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.TextField(blank=True, default='')),
                ('description', models.TextField(blank=True, default='')),
                ('reference', models.CharField(blank=True, default='', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='FormSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Form')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='InputType',
            fields=[
                ('inputtype', models.CharField(blank=True, default='', max_length=256, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='', max_length=256)),
                ('value', models.CharField(blank=True, default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default='')),
                ('datatype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.DataType')),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.List')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Item')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('organisation', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('website', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('phase', models.CharField(max_length=16, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.TextField(blank=True, default='')),
                ('guidance', models.TextField(blank=True, default='')),
                ('warning', models.TextField(blank=True, default='')),
                ('detail', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Field')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Question')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.TextField(blank=True, default='')),
                ('guidance', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='SectionQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Question')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.AddField(
            model_name='section',
            name='questions',
            field=models.ManyToManyField(through='forms.SectionQuestion', to='forms.Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='fields',
            field=models.ManyToManyField(through='forms.QuestionField', to='forms.Field'),
        ),
        migrations.AddField(
            model_name='list',
            name='items',
            field=models.ManyToManyField(through='forms.ListItem', to='forms.Item'),
        ),
        migrations.AddField(
            model_name='formsection',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='form',
            name='organisations',
            field=models.ManyToManyField(to='forms.Organisation'),
        ),
        migrations.AddField(
            model_name='form',
            name='phase',
            field=models.ForeignKey(default='alpha', on_delete=django.db.models.deletion.CASCADE, to='forms.Phase'),
        ),
        migrations.AddField(
            model_name='form',
            name='sections',
            field=models.ManyToManyField(through='forms.FormSection', to='forms.Section'),
        ),
        migrations.AddField(
            model_name='field',
            name='blacklists',
            field=models.ManyToManyField(blank=True, related_name='blacklists', to='forms.List'),
        ),
        migrations.AddField(
            model_name='field',
            name='datatype',
            field=models.ForeignKey(default='string', on_delete=django.db.models.deletion.CASCADE, to='forms.DataType'),
        ),
        migrations.AddField(
            model_name='field',
            name='inputtype',
            field=models.ForeignKey(default='text', on_delete=django.db.models.deletion.CASCADE, to='forms.InputType'),
        ),
        migrations.AddField(
            model_name='field',
            name='whitelists',
            field=models.ManyToManyField(blank=True, related_name='whitelists', to='forms.List'),
        ),
    ]
