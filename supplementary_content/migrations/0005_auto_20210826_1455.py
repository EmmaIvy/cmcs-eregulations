# Generated by Django 3.2.5 on 2021-08-26 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplementary_content', '0004_supplementarycontent_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='supplementary_content.category'),
        ),
    ]
