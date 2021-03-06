# Generated by Django 3.0 on 2022-02-08 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
