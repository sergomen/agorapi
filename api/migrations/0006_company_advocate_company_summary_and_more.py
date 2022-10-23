# Generated by Django 4.1.2 on 2022-10-19 12:35

from django.db import migrations, models
import url_or_relative_url_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_advocate_link_delete_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='advocate',
            field=models.ManyToManyField(blank=True, related_name='advocates', to='api.advocate'),
        ),
        migrations.AddField(
            model_name='company',
            name='summary',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='advocate',
            name='company',
            field=models.ManyToManyField(blank=True, related_name='companies', to='api.company'),
        ),
        migrations.AlterField(
            model_name='company',
            name='href',
            field=url_or_relative_url_field.fields.URLOrRelativeURLField(default='/companies/id'),
        ),
    ]
