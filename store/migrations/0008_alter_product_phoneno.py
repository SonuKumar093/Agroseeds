# Generated by Django 3.2.25 on 2024-05-09 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_feedback_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='phoneno',
            field=models.CharField(default='+916304572667', max_length=10),
        ),
    ]
