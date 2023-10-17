# Generated by Django 4.1.6 on 2023-10-16 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewRelease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='タイトル')),
                ('artist', models.CharField(max_length=100, verbose_name='アーティスト')),
                ('release_date', models.DateField(verbose_name='リリース日')),
                ('url', models.URLField(verbose_name='リンク')),
                ('type', models.CharField(max_length=100, verbose_name='タイプ')),
                ('genre', models.CharField(max_length=100, verbose_name='ジャンル')),
            ],
            options={
                'verbose_name': 'リリース情報',
                'verbose_name_plural': 'リリース情報',
                'db_table': 'new_release',
            },
        ),
    ]
