from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
        ('inventory', '0001_initial'),
    ]
    operations = [
    migrations.RenameField(
        model_name='product',
        old_name='name',
        new_name='name',
    ),
]
    migrations.AlterField(
        model_name='product',
        name='vendor',
        field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.Vendor'),
    ),
