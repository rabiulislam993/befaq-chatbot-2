# Generated by Django 2.0.4 on 2018-05-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='result_json',
            new_name='result',
        ),
        migrations.AlterField(
            model_name='result',
            name='exam_year',
            field=models.IntegerField(choices=[(2015, '২০১৫'), (2016, '২০১৬'), (2017, '২০১৭'), (2018, '২০১৮')], default=2018),
        ),
        migrations.AlterField(
            model_name='result',
            name='student_marhala',
            field=models.IntegerField(choices=[(1, 'তাকমিল'), (2, 'ফযীলত'), (3, 'সানাবিয়া উলইয়া'), (5, 'মুতাওয়াসসিতাহ'), (6, 'ইবতিদাইয়্যাহ'), (7, 'হিফযুল কুরআন'), (8, 'ইলমুত তাজবীদ ওয়াল কিরাআত')], default=1),
        ),
    ]
