# Generated by Django 2.1.4 on 2018-12-30 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_button'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='button',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Button', verbose_name='Botão'),
        ),
    ]
