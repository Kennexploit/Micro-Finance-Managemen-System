# Generated by Django 4.2.7 on 2023-11-16 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_applicant_a_id_alter_applicant_a_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='Created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]