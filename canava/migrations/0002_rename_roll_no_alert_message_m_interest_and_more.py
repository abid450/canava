# Generated by Django 5.1.1 on 2024-09-24 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canava', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert_message_m',
            old_name='Roll_no',
            new_name='interest',
        ),
        migrations.RemoveField(
            model_name='alert_message_m',
            name='city',
        ),
        migrations.RemoveField(
            model_name='alert_message_m',
            name='gender_choice',
        ),
        migrations.AddField(
            model_name='alert_message_m',
            name='age',
            field=models.CharField(choices=[('19 or Older', '19 or Older'), ('Under 19', 'Under 19')], default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alert_message_m',
            name='biography',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alert_message_m',
            name='job_role',
            field=models.CharField(choices=[('Business Owner', 'Business Owner'), ('Android Developer', 'Android Developer'), ('Freelancer', 'Freelancer'), ('Mobile Designer', 'Mobile Designer'), ('Front-End Developer', 'Front-End Developer'), ('WordPress Developer', 'WordPress Developer'), ('Python Developer', 'Python Developer'), ('Web Designer', 'Web Designer'), ('PHP Developer', 'PHP Developer'), ('Django Developer', 'Django Developer'), ('iOS Developer', 'iOS Developer')], default=1, max_length=150),
            preserve_default=False,
        ),
    ]
