# Generated by Django 4.2.7 on 2024-03-13 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferralCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='code_name')),
                ('description', models.TextField(verbose_name='description')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='date created')),
                ('lifetime', models.PositiveSmallIntegerField(default=1, verbose_name='lifetime')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('user_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('user_subscriber', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='subscriber', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'referral code',
                'verbose_name_plural': 'referral',
                'ordering': ['-date_created'],
            },
        ),
    ]
