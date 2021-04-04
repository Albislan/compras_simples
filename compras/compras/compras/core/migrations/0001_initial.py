# Generated by Django 3.1.4 on 2021-04-02 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('forn_number', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=70)),
                ('observacoes', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'fornecedor',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='ContatoFornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contato', models.CharField(max_length=20, verbose_name='Nome do Contato')),
                ('observacoes', models.CharField(max_length=100)),
                ('empresa', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='core.fornecedor')),
            ],
            options={
                'db_table': 'contatos',
                'ordering': ('contato',),
            },
        ),
    ]
