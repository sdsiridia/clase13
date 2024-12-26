# Generated by Django 5.1.2 on 2024-12-22 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_editorial_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autores',
            field=models.ManyToManyField(blank=True, null=True, to='books.autor'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='idioma',
            field=models.CharField(blank=True, choices=[('ES', 'Español'), ('EN', 'Inglés')], default='ES', max_length=2, null=True),
        ),
    ]