# Generated by Django 4.2.7 on 2023-11-16 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_date_applied_loan_applied_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='applied',
            new_name='created',
        ),
    ]
