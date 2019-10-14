# Generated by Django 2.2.6 on 2019-10-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0007_bookinstance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barrower',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('issue_date', models.DateField(null=True)),
                ('due_date', models.DateField(null=True)),
                ('date_return', models.DateField(null=True)),
                ('availability', models.BooleanField()),
                ('card', models.ForeignKey(on_delete='on_delete=model.CASCADE', to='libraryapp.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_return', models.DateField(null=True)),
                ('availability', models.BooleanField()),
                ('book', models.ForeignKey(on_delete='on_delete=models.CASCADE', to='libraryapp.Book')),
                ('name', models.ForeignKey(on_delete='on_delete=model.CASCADE', to='libraryapp.Student')),
            ],
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
    ]