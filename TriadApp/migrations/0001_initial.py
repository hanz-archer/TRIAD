# Generated by Django 5.1.4 on 2025-01-14 01:32

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='stall_logos/')),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
    ]
