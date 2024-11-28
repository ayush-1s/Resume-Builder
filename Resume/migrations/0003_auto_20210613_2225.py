# Generated by Django 3.1.1 on 2021-06-13 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0002_auto_20210613_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_Current',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='uni_Start',
            field=models.DateField(blank=True, null=True, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_Progress',
            field=models.CharField(blank=True, choices=[('3', 'Pending'), ('0', '---'), ('2', 'In Progress'), ('1', 'Completed')], default='0', help_text='Complete, In Progress, Pending', max_length=200, verbose_name='Progress'),
        ),
    ]
