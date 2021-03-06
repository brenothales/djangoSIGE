# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-25 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendas', '0001_initial'),
        ('cadastro', '0001_initial'),
        ('compras', '0001_initial'),
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='cond_pagamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compra_pagamento', to='vendas.CondicaoPagamento'),
        ),
        migrations.AddField(
            model_name='compra',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compra_fornecedor', to='cadastro.Fornecedor'),
        ),
        migrations.AddField(
            model_name='compra',
            name='local_dest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='compra_local_estoque', to='estoque.LocalEstoque'),
        ),
        migrations.AddField(
            model_name='pedidocompra',
            name='orcamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orcamento_pedido', to='compras.OrcamentoCompra'),
        ),
    ]
