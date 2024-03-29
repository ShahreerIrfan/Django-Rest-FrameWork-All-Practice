# Generated by Django 4.2.7 on 2024-02-19 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show_car', '0008_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CarName', models.CharField(max_length=50)),
                ('CarPrice', models.IntegerField()),
                ('Category', models.CharField(choices=[('sedan', 'Sedan'), ('hatchback', 'Hatchback'), ('SUV', 'SUV'), ('truck', 'Truck'), ('electric', 'Electric')], max_length=50)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Review', to='show_car.carlist'),
        ),
    ]
