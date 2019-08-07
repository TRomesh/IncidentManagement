# Generated by Django 2.2.1 on 2019-07-16 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190716_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='action',
            field=models.CharField(choices=[('CREATED', 'Created'), ('GENERIC_UPDATE', 'Generic Update'), ('ATTRIBUTE_CHANGE_REQUESTED', 'Attribute change requested'), ('ATTRIBUTE_CHANGE_APPROVED', 'Attribute change approved'), ('ATTRIBUTE_CHANGED', 'Attribute changed'), ('ATTRIBUTE_CHANGE_REJECTED', 'Attribute change rejected'), ('COMMENTED', 'Commented'), ('OUTCOME_ADDED', 'Outcome added'), ('ENTITY_ASSIGNED', 'Entity assigned'), ('ENTITY_REMOVED', 'Entity removed'), ('ACTION_STARTED', 'Started Action'), ('ACTION_COMPLETED', 'Ended Action')], max_length=50),
        ),
    ]