# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=8, blank=True)),
                ('condition', models.CharField(default='b', max_length=1, choices=[('a', 'Pristine'), ('b', 'Used, good'), ('c', 'Used, worn'), ('d', 'Cracked / chipped'), ('e', 'Broken')])),
            ],
            options={
                'verbose_name': 'condition',
                'verbose_name_plural': 'conditions',
            },
        ),
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('documentation_name', models.CharField(max_length=8, blank=True)),
            ],
            options={
                'verbose_name': 'documentation',
                'verbose_name_plural': 'documentation',
            },
        ),
        migrations.CreateModel(
            name='documentation_link_piece',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('documentation_date', models.DateField(null=True, blank=True)),
                ('documentation_author', models.CharField(max_length=8, blank=True)),
                ('documentation_media', models.CharField(max_length=8, blank=True)),
                ('documentation_location', models.CharField(max_length=8, blank=True)),
                ('documentation', models.ForeignKey(to='somepots.Documentation')),
            ],
            options={
                'verbose_name': 'documentation link',
                'verbose_name_plural': 'documentation pieces',
            },
        ),
        migrations.CreateModel(
            name='exhibition_link_piece',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
                'verbose_name': 'exhibition link',
                'verbose_name_plural': 'exhibition pieces',
            },
        ),
        migrations.CreateModel(
            name='ExhibitionLookup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('exhibition_name', models.CharField(max_length=8, blank=True)),
                ('exhibition_date', models.DateField(null=True, blank=True)),
                ('exhibition_description', models.CharField(max_length=12, blank=True)),
            ],
            options={
                'verbose_name': 'exhibition',
                'verbose_name_plural': 'exhibitions',
            },
        ),
        migrations.CreateModel(
            name='glaze_link_piece',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('batch', models.CharField(default='200', max_length=12)),
            ],
            options={
                'verbose_name': 'glaze link',
                'verbose_name_plural': 'glaze pieces',
            },
        ),
        migrations.CreateModel(
            name='GlazeLookup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('glaze_name', models.CharField(default='boola', unique=True, max_length=8)),
                ('glaze_description', models.CharField(max_length=12, blank=True)),
                ('glaze_begin_date', models.DateField(null=True, blank=True)),
                ('glaze_end_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'glaze',
                'verbose_name_plural': 'glazes',
            },
        ),
        migrations.CreateModel(
            name='heath_line_link_piece',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('feature', models.CharField(default='too true', max_length=12)),
            ],
            options={
                'verbose_name': 'heath line link',
                'verbose_name_plural': 'heath line pieces',
            },
        ),
        migrations.CreateModel(
            name='HeathLineLookup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('heath_line_name', models.CharField(max_length=8, blank=True)),
                ('heath_line_begin_date', models.DateField(null=True, blank=True)),
                ('heath_line_end_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'heath line ',
                'verbose_name_plural': 'heath lines',
            },
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Logo_name', models.CharField(max_length=8, blank=True)),
                ('logo_description', models.CharField(max_length=12, blank=True)),
                ('stamp_name', models.CharField(max_length=8, blank=True)),
                ('picture', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'logo',
                'verbose_name_plural': 'logos',
            },
        ),
        migrations.CreateModel(
            name='logo_link_piece',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('feature', models.CharField(default='too true', max_length=12)),
                ('Logo', models.ForeignKey(to='somepots.Logo')),
            ],
        ),
        migrations.CreateModel(
            name='maker_link_piece',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('feature', models.CharField(default='too true', max_length=12)),
            ],
            options={
                'verbose_name': 'maker link',
                'verbose_name_plural': 'maker pieces',
            },
        ),
        migrations.CreateModel(
            name='MakerLookup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('maker_name', models.CharField(max_length=8, blank=True)),
                ('maker_location', models.CharField(max_length=8, blank=True)),
                ('maker_start_date', models.DateField(null=True, blank=True)),
                ('maker_stop_date', models.DateField(null=True, blank=True)),
                ('maker_description', models.CharField(max_length=12, blank=True)),
            ],
            options={
                'verbose_name': 'maker',
                'verbose_name_plural': 'makers',
            },
        ),
        migrations.CreateModel(
            name='material_link_piece',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('feature', models.CharField(default='too true', max_length=12)),
            ],
            options={
                'verbose_name': 'material link',
                'verbose_name_plural': 'material pieces',
            },
        ),
        migrations.CreateModel(
            name='MaterialLookup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('material_name', models.CharField(max_length=8, blank=True)),
                ('material_description', models.CharField(max_length=12, blank=True)),
            ],
            options={
                'verbose_name': 'material',
                'verbose_name_plural': 'materials',
            },
        ),
        migrations.CreateModel(
            name='method_link_piece',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('feature', models.CharField(default='too true', max_length=12)),
            ],
            options={
                'verbose_name': 'method link',
                'verbose_name_plural': 'method pieces',
            },
        ),
        migrations.CreateModel(
            name='MethodLookup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('method_name', models.CharField(max_length=8, blank=True)),
                ('method_description', models.CharField(max_length=12, blank=True)),
            ],
            options={
                'verbose_name': 'method',
                'verbose_name_plural': 'methods',
            },
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('post_edith', models.NullBooleanField()),
                ('catalogue_id', models.CharField(max_length=8)),
                ('heath_id', models.CharField(max_length=8, blank=True)),
                ('piece_name', models.CharField(max_length=6, blank=True)),
                ('piece_description', models.CharField(max_length=12, blank=True)),
                ('manufactured_date', models.DateField(null=True, blank=True)),
                ('length_inches', models.IntegerField(null=True, blank=True)),
                ('width_inches', models.IntegerField(null=True, blank=True)),
                ('height_inches', models.IntegerField(null=True, blank=True)),
                ('weight_ounces', models.IntegerField(null=True, blank=True)),
                ('length_mm', models.IntegerField(null=True, blank=True)),
                ('width_mm', models.IntegerField(null=True, blank=True)),
                ('height_mm', models.IntegerField(null=True, blank=True)),
                ('weight_grams', models.IntegerField(null=True, blank=True)),
                ('cataloguer', models.CharField(max_length=8, blank=True)),
                ('catalogue_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'piece',
                'verbose_name_plural': 'pieces',
            },
        ),
        migrations.CreateModel(
            name='publication_link_piece',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField(null=True, blank=True)),
                ('description', models.CharField(max_length=8, blank=True)),
                ('publication_author', models.CharField(max_length=8, blank=True)),
                ('piece', models.ForeignKey(to='somepots.Piece')),
            ],
            options={
                'verbose_name': 'publication link',
                'verbose_name_plural': 'publication pieces',
            },
        ),
        migrations.CreateModel(
            name='PublicationLookup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('publication_name', models.CharField(max_length=8, blank=True)),
                ('publication_date', models.DateField(null=True, blank=True)),
                ('publication_author', models.CharField(max_length=8, blank=True)),
                ('publication_media', models.CharField(max_length=8, blank=True)),
            ],
            options={
                'verbose_name': 'publication',
                'verbose_name_plural': 'publications',
            },
        ),
        migrations.CreateModel(
            name='SetCollection',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('set_collection_name', models.CharField(max_length=8, blank=True)),
                ('setcollection_location', models.CharField(max_length=8, blank=True)),
            ],
            options={
                'verbose_name': 'collection',
                'verbose_name_plural': 'collections',
            },
        ),
        migrations.CreateModel(
            name='setCollection_link_piece',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField(null=True, blank=True)),
                ('description', models.CharField(max_length=12, blank=True)),
                ('Piece', models.ForeignKey(to='somepots.Piece')),
                ('SetCollection', models.ForeignKey(to='somepots.SetCollection')),
            ],
            options={
                'verbose_name': 'collection link',
                'verbose_name_plural': 'collection pieces',
            },
        ),
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='setcollection',
            name='set_collection_piece',
            field=models.ManyToManyField(to='somepots.Piece', through='somepots.setCollection_link_piece'),
        ),
        migrations.AddField(
            model_name='publication_link_piece',
            name='publication',
            field=models.ForeignKey(to='somepots.PublicationLookup'),
        ),
        migrations.AddField(
            model_name='methodlookup',
            name='method_pieces',
            field=models.ManyToManyField(to='somepots.Piece', through='somepots.method_link_piece'),
        ),
        migrations.AddField(
            model_name='method_link_piece',
            name='MethodLookup',
            field=models.ForeignKey(to='somepots.MethodLookup'),
        ),
        migrations.AddField(
            model_name='method_link_piece',
            name='Piece',
            field=models.ForeignKey(to='somepots.Piece'),
        ),
        migrations.AddField(
            model_name='materiallookup',
            name='material_pieces',
            field=models.ManyToManyField(to='somepots.Piece', through='somepots.material_link_piece'),
        ),
        migrations.AddField(
            model_name='material_link_piece',
            name='MaterialLookup',
            field=models.ForeignKey(to='somepots.MaterialLookup'),
        ),
        migrations.AddField(
            model_name='material_link_piece',
            name='Piece',
            field=models.ForeignKey(to='somepots.Piece'),
        ),
        migrations.AddField(
            model_name='makerlookup',
            name='maker_pieces',
            field=models.ManyToManyField(to='somepots.Piece', through='somepots.maker_link_piece'),
        ),
        migrations.AddField(
            model_name='maker_link_piece',
            name='MakerLookup',
            field=models.ForeignKey(to='somepots.MakerLookup'),
        ),
        migrations.AddField(
            model_name='maker_link_piece',
            name='Piece',
            field=models.ForeignKey(to='somepots.Piece'),
        ),
        migrations.AddField(
            model_name='logo_link_piece',
            name='Piece',
            field=models.ForeignKey(to='somepots.Piece'),
        ),
        migrations.AddField(
            model_name='logo',
            name='logo_pieces',
            field=models.ManyToManyField(to='somepots.Piece', through='somepots.logo_link_piece'),
        ),
        migrations.AddField(
            model_name='heathlinelookup',
            name='heath_line_pieces',
            field=models.ManyToManyField(to='somepots.Piece', through='somepots.heath_line_link_piece'),
        ),
        migrations.AddField(
            model_name='heath_line_link_piece',
            name='heath_line',
            field=models.ForeignKey(to='somepots.HeathLineLookup'),
        ),
        migrations.AddField(
            model_name='heath_line_link_piece',
            name='piece',
            field=models.ForeignKey(to='somepots.Piece'),
        ),
        migrations.AddField(
            model_name='glazelookup',
            name='glaze_pieces',
            field=models.ManyToManyField(to='somepots.Piece', through='somepots.glaze_link_piece'),
        ),
        migrations.AddField(
            model_name='glaze_link_piece',
            name='glazeLookup',
            field=models.ForeignKey(to='somepots.GlazeLookup'),
        ),
        migrations.AddField(
            model_name='glaze_link_piece',
            name='piece',
            field=models.ForeignKey(to='somepots.Piece'),
        ),
        migrations.AddField(
            model_name='exhibition_link_piece',
            name='exhibition',
            field=models.ForeignKey(to='somepots.ExhibitionLookup'),
        ),
        migrations.AddField(
            model_name='exhibition_link_piece',
            name='piece',
            field=models.ForeignKey(to='somepots.Piece'),
        ),
        migrations.AddField(
            model_name='documentation_link_piece',
            name='piece',
            field=models.ForeignKey(to='somepots.Piece'),
        ),
        migrations.AddField(
            model_name='documentation',
            name='documentation_pieces',
            field=models.ManyToManyField(to='somepots.Piece', through='somepots.documentation_link_piece'),
        ),
    ]
