# Generated by Django 4.1.7 on 2023-03-02 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_solicitacao_celular_alter_solicitacao_nuvem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitacao',
            name='celular',
        ),
        migrations.RemoveField(
            model_name='solicitacao',
            name='nuvem',
        ),
        migrations.AddField(
            model_name='celular',
            name='solicitacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='celular', to='api.solicitacao'),
            preserve_default=False,
        ),
    ]
