# Generated by Django 4.0.3 on 2022-05-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0004_remove_itempedido_cor_remove_itempedido_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='transaction_code',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(default='Aguardando', max_length=13),
        ),
    ]
