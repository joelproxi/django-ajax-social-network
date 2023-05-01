# Generated by Django 4.1.6 on 2023-04-29 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps', '0005_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifaication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255)),
                ('read', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('object_id', models.IntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='obj', to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddIndex(
            model_name='notifaication',
            index=models.Index(fields=['-created'], name='apps_notifa_created_c6f473_idx'),
        ),
        migrations.AddIndex(
            model_name='notifaication',
            index=models.Index(fields=['content_type', 'object_id'], name='apps_notifa_content_69d9b1_idx'),
        ),
    ]