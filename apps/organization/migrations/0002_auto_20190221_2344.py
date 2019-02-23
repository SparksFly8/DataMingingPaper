# Generated by Django 2.0.1 on 2019-02-21 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='desc',
            field=models.TextField(default='这个机构很懒，什么都没留下来', verbose_name='机构描述'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='points',
            field=models.CharField(default='无', max_length=50, verbose_name='教学特点'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CityDict', verbose_name='所在城市'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='name',
            field=models.CharField(max_length=50, verbose_name='机构名称'),
        ),
    ]