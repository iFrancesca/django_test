# Generated by Django 3.2.12 on 2022-03-04 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255, verbose_name='标题')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('website', models.URLField(verbose_name='链接')),
                ('content', models.CharField(max_length=500, verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='作者')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
