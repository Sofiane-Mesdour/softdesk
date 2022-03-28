# Generated by Django 3.1.7 on 2021-03-16 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0005_auto_20210312_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='desc',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('a faire', 'À faire'), ('en cours', 'En Cours'), ('termine', 'Terminé')], max_length=128),
        ),
        migrations.AddConstraint(
            model_name='contributor',
            constraint=models.UniqueConstraint(fields=('user', 'project'), name='unique_user'),
        ),
    ]