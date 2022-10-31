# Generated by Django 4.1.2 on 2022-10-30 16:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_rename_footertext_footer_footertext'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footer',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='footer',
            name='mail',
            field=models.EmailField(max_length=50),
        ),
    ]