# Generated by Django 3.2.3 on 2021-07-13 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_svg', models.FileField(upload_to='images/svg')),
                ('Image_png', models.FileField(upload_to='images/png')),
                ('name', models.CharField(max_length=50)),
                ('Desc', models.TextField(max_length=500)),
            ],
        ),
    ]
