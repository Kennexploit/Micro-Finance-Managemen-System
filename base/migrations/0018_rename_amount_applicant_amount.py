# Generated by Django 4.2.7 on 2023-11-17 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_rename_your_amount_applicant_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='amount',
            new_name='Amount',
        ),
    ]