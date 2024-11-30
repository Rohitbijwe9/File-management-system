# Generated by Django 4.2.3 on 2023-09-23 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file_content',
        ),
        migrations.RemoveField(
            model_name='file',
            name='owner',
        ),
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default=False, upload_to='uploads/'),
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent_folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='file_manager.folder')),
            ],
        ),
        migrations.AlterField(
            model_name='file',
            name='parent_folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='file_manager.folder'),
        ),
    ]
