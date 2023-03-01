# Generated by Django 4.1.7 on 2023-02-28 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_apreensao', models.CharField(blank=True, max_length=50, null=True)),
                ('n_item', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo_dispositivo', models.CharField(max_length=50)),
                ('marca_dispositivo', models.CharField(max_length=50)),
                ('modelo_dispositivo', models.CharField(max_length=50)),
                ('imei_dispositivo', models.CharField(max_length=50)),
                ('obs_entrada', models.CharField(blank=True, max_length=500, null=True)),
                ('lacre_entrada', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Celular',
                'verbose_name_plural': 'Celulares',
            },
        ),
        migrations.CreateModel(
            name='Nuvem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=50)),
                ('usuario', models.CharField(max_length=150)),
                ('bsid', models.CharField(max_length=150)),
                ('obs_entrada', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name': 'nuvem',
                'verbose_name_plural': 'nuvens',
            },
        ),
        migrations.CreateModel(
            name='Operacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('criador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operacao_criador', to=settings.AUTH_USER_MODEL)),
                ('integrantes', models.ManyToManyField(related_name='operacao_integrantes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Operacao',
                'verbose_name_plural': 'Operacoes',
            },
        ),
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Nuvem', 'Nuvem'), ('Celular', 'Celular')], max_length=50)),
                ('situacao', models.CharField(max_length=50)),
                ('data_entrada', models.DateField(default=django.utils.timezone.now)),
                ('ipl', models.CharField(blank=True, max_length=50, null=True)),
                ('referencia', models.CharField(blank=True, max_length=120, null=True)),
                ('oficio_entrada', models.CharField(blank=True, max_length=120, null=True)),
                ('autorizacao_judicial', models.CharField(blank=True, max_length=200, null=True)),
                ('Solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitacoes', to=settings.AUTH_USER_MODEL)),
                ('celular', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='solicitacao', to='api.celular')),
                ('nuvem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='solicitacao', to='api.nuvem')),
                ('operacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitacao', to='api.operacao')),
            ],
            options={
                'verbose_name': 'Solicitacao',
                'verbose_name_plural': 'Solicitacoes',
            },
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_saida', models.DateTimeField(default=django.utils.timezone.now)),
                ('oficio_saida', models.CharField(blank=True, max_length=50, null=True)),
                ('destinatario', models.CharField(max_length=50)),
                ('obs_saida', models.CharField(blank=True, max_length=500, null=True)),
                ('resultados', models.CharField(blank=True, max_length=500, null=True)),
                ('lacre_saida', models.CharField(blank=True, max_length=50, null=True)),
                ('n_ipj', models.CharField(blank=True, max_length=50, null=True)),
                ('hash', models.CharField(blank=True, max_length=50, null=True)),
                ('solicitacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='resposta', to='api.solicitacao')),
            ],
            options={
                'verbose_name': 'resposta',
                'verbose_name_plural': 'respostas',
            },
        ),
    ]
