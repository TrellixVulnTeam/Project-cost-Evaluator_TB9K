# Generated by Django 2.2.1 on 2019-07-09 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('concept_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('concept_name', models.CharField(max_length=30)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='work',
            name='percent',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employid', to='cost.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Concept_work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.FloatField(null=True)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conceptid', to='cost.Concept')),
                ('empl_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emplo', to='cost.Employee')),
            ],
        ),
    ]