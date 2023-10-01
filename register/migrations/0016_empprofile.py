# Generated by Django 3.1.4 on 2021-04-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0015_auto_20201212_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satisfaction_level', models.FloatField()),
                ('last_evaluation', models.FloatField()),
                ('num_projects', models.IntegerField()),
                ('avg_monthly_hrs', models.IntegerField()),
                ('time_spent_company', models.IntegerField()),
                ('work_accident', models.IntegerField()),
                ('promotion_last_5_years', models.IntegerField()),
                ('departments', models.CharField(choices=[('0', 'IT'), ('1', 'R&D'), ('2', 'Accounting'), ('3', 'HR'), ('4', 'Management'), ('5', 'Marketing'), ('6', 'Product Management'), ('7', 'Sales'), ('8', 'Support'), ('9', 'Technical')], default=1, max_length=7)),
                ('salary_level', models.CharField(choices=[('1', 'Low'), ('2', 'Medium'), ('3', 'High')], default=1, max_length=7)),
            ],
        ),
    ]
