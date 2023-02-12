# Generated by Django 4.1.6 on 2023-02-12 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(verbose_name='description')),
                ('poster', models.ImageField(null=True, upload_to='clubsPoster/')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('surname', models.CharField(max_length=90)),
                ('birth', models.DateField(blank=True)),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(blank=True, upload_to='playersImage/')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oneXbet.club')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(blank=True)),
                ('result1', models.PositiveSmallIntegerField(default=0)),
                ('result2', models.PositiveSmallIntegerField(default=0)),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('club1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='club1_id', to='oneXbet.club')),
                ('club2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oneXbet.club')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneXbet.league'),
        ),
        migrations.CreateModel(
            name='Betting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw', models.BooleanField(blank=True, default=False)),
                ('money', models.PositiveIntegerField(blank=True)),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oneXbet.club')),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oneXbet.game')),
            ],
        ),
    ]
