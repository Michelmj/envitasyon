from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seatingguest',
            name='seat',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
