# Generated by Django 2.1.1 on 2018-09-27 04:45

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
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_1', models.CharField(blank=True, max_length=20, null=True, verbose_name='サンプル項目1_文字列')),
                ('sample_2', models.IntegerField(blank=True, null=True, verbose_name='サンプル項目2_数値')),
                ('sample_3', models.BooleanField(verbose_name='サンプル項目3_ブール値')),
                ('sample_4', models.IntegerField(blank=True, choices=[(1, '選択１'), (2, '選択２'), (3, '選択３')], null=True, verbose_name='サンプル項目4_選択肢')),
                ('sample_5', models.DateField(blank=True, null=True, verbose_name='サンプル項目5 日付')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='作成時間')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='更新時間')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CreatedBy', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UpdatedBy', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': 'サンプル',
                'verbose_name_plural': 'サンプル',
            },
        ),
    ]
