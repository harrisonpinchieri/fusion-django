# Generated by Django 4.2.4 on 2023-08-16 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_servico_icone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-mobile', 'Mobile'), ('lni-Stats-up', 'Gráfico'), ('lni-cog', 'Engrenagem'), ('lni-layers', 'Design'), ('lni-rocket', 'Foguete'), ('lni-users', 'Usuários')], max_length=12, verbose_name='Icone'),
        ),
    ]