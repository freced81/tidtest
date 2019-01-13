# Generated by Django 2.1.5 on 2019-01-11 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("tid_rapport", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="kund",
            name="kund_kontakt_person",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.RemoveField(model_name="projekt", name="arbetsplats"),
        migrations.AddField(
            model_name="projekt",
            name="arbetsplats",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tid_rapport.Arbetsplats",
            ),
        ),
        migrations.RemoveField(model_name="projekt", name="kund"),
        migrations.AddField(
            model_name="projekt",
            name="kund",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tid_rapport.Kund",
            ),
        ),
    ]