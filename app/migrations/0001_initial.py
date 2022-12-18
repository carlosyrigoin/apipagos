# Generated by Django 4.1.4 on 2022-12-18 14:49

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
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('logo', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18)),
                ('paymentdate', models.DateField(auto_now=True)),
                ('expirationdate', models.DateField()),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.services')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='expired_payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalty_free_amount', models.DecimalField(decimal_places=2, max_digits=18)),
                ('pay_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.payment_user')),
            ],
        ),
    ]
