# Generated by Django 4.2.16 on 2024-11-24 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepositProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=6)),
                ('fin_co_no', models.CharField(max_length=10)),
                ('fin_prdt_cd', models.CharField(max_length=50)),
                ('kor_co_nm', models.CharField(max_length=100)),
                ('fin_prdt_nm', models.CharField(max_length=100)),
                ('join_way', models.CharField(max_length=100)),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.CharField(max_length=1)),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.BigIntegerField(null=True)),
                ('dcls_strt_day', models.CharField(max_length=8)),
                ('dcls_end_day', models.CharField(max_length=8, null=True)),
                ('fin_co_subm_day', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='SavingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=6)),
                ('fin_co_no', models.CharField(max_length=20)),
                ('fin_prdt_cd', models.CharField(max_length=100)),
                ('kor_co_nm', models.CharField(max_length=100)),
                ('fin_prdt_nm', models.CharField(max_length=100)),
                ('join_way', models.TextField()),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.CharField(max_length=1)),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.BigIntegerField(null=True)),
                ('dcls_strt_day', models.CharField(max_length=8)),
                ('dcls_end_day', models.CharField(max_length=8, null=True)),
                ('fin_co_subm_day', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='SavingOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=6)),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type', models.TextField()),
                ('intr_rate', models.FloatField()),
                ('save_trm', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='finlife.savingproduct')),
            ],
        ),
        migrations.CreateModel(
            name='DepositOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=6)),
                ('fin_co_no', models.CharField(max_length=10)),
                ('fin_prdt_cd', models.CharField(max_length=50)),
                ('intr_rate_type', models.CharField(max_length=1)),
                ('intr_rate_type_nm', models.CharField(max_length=10)),
                ('save_trm', models.IntegerField()),
                ('intr_rate', models.FloatField()),
                ('intr_rate2', models.FloatField()),
                ('rsrv_type', models.CharField(blank=True, max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='finlife.depositproduct')),
            ],
        ),
    ]
