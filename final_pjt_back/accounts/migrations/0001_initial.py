
import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('birth_date', models.DateField(default=datetime.date(1900, 1, 1))),
                ('gender', models.CharField(choices=[('M', '남성'), ('F', '여성')], default='M', max_length=1, verbose_name='성별')),
                ('member_type', models.CharField(choices=[('regular', '일반회원'), ('expert', '전문가회원')], default='regular', max_length=10)),
                ('terms_agreement', models.BooleanField(default=False)),
                ('privacy_agreement', models.BooleanField(default=False)),
                ('agreement_date', models.DateTimeField(blank=True, null=True)),
                ('income_level', models.CharField(choices=[('low', '저소득층 (월 소득 200만원 이하)'), ('middle', '중소득층 (월 소득 200만원 ~ 700만원)'), ('high', '고소득층 (월 소득 700만원 이상)')], default='middle', max_length=10, verbose_name='소득수준')),
                ('total_score', models.IntegerField(blank=True, null=True, verbose_name='금융성향 점수')),
                ('age_score', models.IntegerField(blank=True, null=True, verbose_name='연령대 점수')),
                ('income_score', models.IntegerField(blank=True, null=True, verbose_name='소득수준 점수')),
                ('consumption_score', models.IntegerField(blank=True, null=True, verbose_name='소비습관 점수')),
                ('test_date', models.DateTimeField(blank=True, null=True, verbose_name='테스트 진행일')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
