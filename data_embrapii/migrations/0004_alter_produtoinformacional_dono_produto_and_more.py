# Generated by Django 5.1 on 2024-09-23 12:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_embrapii', '0003_produtoinformacional_dono_produto_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtoinformacional',
            name='dono_produto',
            field=models.CharField(blank=True, choices=[('nao_informado', 'Não Informado'), ('ged_dpg', 'GED/DPG')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produtoinformacional',
            name='ferramenta',
            field=models.CharField(blank=True, choices=[('nao_informado', 'Não Informado'), ('ms_power_bi', 'Microsoft Power BI'), ('ms_excel', 'Microsoft Excel'), ('ms_word', 'Microsoft Word'), ('canva', 'Canva'), ('pdf', 'PDF'), ('google_looker', 'Google Looker')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produtoinformacional',
            name='fonte_dados',
            field=models.CharField(blank=True, choices=[('nao_informado', 'Não Informado'), ('ged_dpg', 'GED/DPG')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produtoinformacional',
            name='user_atualizacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='produtoinfo_user_atualizacao', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='produtoinformacional',
            name='user_registro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='produtoinfo_user_registro', to=settings.AUTH_USER_MODEL),
        ),
    ]
