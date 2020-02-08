# Generated by Django 3.0.2 on 2020-02-03 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0007_auto_20200123_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='electionevent',
            name='election_mode',
            field=models.SlugField(choices=[('upcoming', 'Upcoming'), ('in-progress', 'In progress')], default='upcoming'),
        ),
        migrations.CreateModel(
            name='ElectionDataURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, editable=False, max_length=500)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, unique=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('url_type', models.SlugField(choices=[('metadata', 'Metadata'), ('polled', 'Frequently-updated data')], default='polled', max_length=15)),
                ('url_descriptor', models.SlugField(max_length=10)),
                ('url_path', models.URLField()),
                ('election_event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='data_urls', to='election.ElectionEvent')),
            ],
            options={
                'unique_together': {('election_event', 'url_descriptor')},
            },
        ),
    ]
