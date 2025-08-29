from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('account', '0001_initial'),  # ← замени на имя последней миграции
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='userid',
            field=models.ForeignKey(
                to='auth.User',
                on_delete=models.CASCADE,
                default=2
            ),
        ),
    ]