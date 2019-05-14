# Generated by Django 2.1.7 on 2019-05-14 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='fk_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canvass.Question'),
        ),
    ]