# Generated by Django 5.1.1 on 2024-10-02 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canava', '0007_alter_alert_message_m_course_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert_message_m',
            name='course_name',
            field=models.CharField(choices=[('Office Management', 'Office Management'), ('Grapics Design', 'Grapics Design'), ('Web Development (Python,Django)', 'Web Development (Python,Django)'), ('Python Programming', 'Python Programming'), ('Digital Marketing', 'Digital Marketing')], max_length=150),
        ),
        migrations.AlterField(
            model_name='alert_message_m',
            name='interest',
            field=models.CharField(choices=[('Business', 'Business'), ('Development', 'Development'), ('Design', 'Design')], max_length=150),
        ),
    ]
