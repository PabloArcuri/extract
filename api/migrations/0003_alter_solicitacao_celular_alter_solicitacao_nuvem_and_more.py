# Generated by Django 4.1.7 on 2023-03-01 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_solicitacao_solicitante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='celular',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='celular_solicitacao', to='api.celular'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='nuvem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='nuvem_solicitacao', to='api.nuvem'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='operacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='op_solicitacao', to='api.operacao'),
        ),
    ]