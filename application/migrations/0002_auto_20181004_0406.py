# Generated by Django 2.1 on 2018-10-04 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='resume/')),
            ],
        ),
        migrations.RemoveField(
            model_name='application',
            name='resume',
        ),
    ]