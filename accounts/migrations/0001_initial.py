# Generated by Django 3.2.5 on 2021-07-09 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation_Tables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_code', models.CharField(max_length=50)),
                ('inv_code_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('sign_in_date', models.DateTimeField(auto_now_add=True)),
                ('FK_inv_code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.invitation_tables')),
            ],
            options={
                'verbose_name_plural': 'Users Table',
            },
        ),
    ]
