# Generated by Django 5.0.6 on 2024-05-25 11:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_product_product_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('rejected', 'Rejected'), ('draft', 'draft'), ('disabled', 'Disabled'), ('published', 'Published')], default='in_review', max_length=10),
        ),
    ]
