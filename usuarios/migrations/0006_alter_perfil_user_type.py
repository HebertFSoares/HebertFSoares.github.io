# Generated by Django 4.2.1 on 2023-05-15 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_perfil_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='user_type',
            field=models.CharField(blank=True, choices=[('e', 'Estudante'), ('a', 'Anfitrião')], max_length=50, null=True),
        ),
    ]