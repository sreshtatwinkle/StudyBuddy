# Generated by Django 4.2.1 on 2023-08-17 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_subject_alter_user_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subject',
            field=models.CharField(choices=[('python', 'python'), ('java', 'java'), ('html,css.js', 'html,css,js'), ('React', 'React'), ('Computer Networks', 'Computer Networks'), ('Databases', 'Databases'), ('C++', 'C++'), ('None', 'None')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]