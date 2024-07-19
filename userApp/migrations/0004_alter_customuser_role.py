# Generated by Django 5.0.6 on 2024-07-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0003_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('admin', 'Admin'), ('unituser', 'UnitUser'), ('headofdepartment', 'HeadofDepartment'), ('headofdivision', 'HeadofDivision')], default='user', max_length=20),
        ),
    ]
