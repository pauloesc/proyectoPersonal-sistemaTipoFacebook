# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IdiomaUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
                'db_table': 'idioma_user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TablaIdioma',
            fields=[
                ('idioma', models.TextField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'tabla_idioma',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TablaLenguaje',
            fields=[
                ('lenguaje', models.TextField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'tabla_lenguaje',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TablaNivel',
            fields=[
                ('nivel', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'tabla_nivel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TablaPregunta',
            fields=[
                ('pregunta_contenido', models.TextField()),
                ('pregunta_fecha', models.DateField()),
                ('pregunta_id', models.AutoField(primary_key=True, serialize=False)),
                ('pregunta_idioma', models.ForeignKey(db_column='pregunta_idioma', to='registro.TablaIdioma')),
                ('pregunta_lenguaje', models.ForeignKey(db_column='pregunta_lenguaje', to='registro.TablaLenguaje')),
                ('pregunta_nivel', models.ForeignKey(db_column='pregunta_nivel', to='registro.TablaNivel')),
            ],
            options={
                'db_table': 'tabla_pregunta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TablaRespuesta',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('respuesta_contenido', models.TextField()),
                ('respuesta_fecha', models.DateField()),
                ('votos', models.IntegerField(null=True, blank=True)),
                ('respuesta', models.ForeignKey(to='registro.TablaPregunta')),
            ],
            options={
                'db_table': 'tabla_respuesta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TablaUsuario',
            fields=[
                ('username', models.TextField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('correo', models.TextField()),
                ('passw', models.TextField()),
            ],
            options={
                'db_table': 'tabla_usuario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UsuarioLenguajeNivel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('user_lenguaje', models.ForeignKey(db_column='user_lenguaje', to='registro.TablaLenguaje')),
                ('user_nivel', models.ForeignKey(db_column='user_nivel', to='registro.TablaNivel')),
                ('user_sabe', models.ForeignKey(db_column='user_sabe', to='registro.TablaUsuario')),
            ],
            options={
                'db_table': 'usuario_lenguaje_nivel',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='tablarespuesta',
            name='respuesta_username',
            field=models.ForeignKey(db_column='respuesta_username', to='registro.TablaUsuario'),
        ),
        migrations.AddField(
            model_name='tablapregunta',
            name='pregunta_user',
            field=models.ForeignKey(db_column='pregunta_user', to='registro.TablaUsuario'),
        ),
        migrations.AddField(
            model_name='idiomauser',
            name='habla',
            field=models.ForeignKey(to='registro.TablaUsuario'),
        ),
        migrations.AddField(
            model_name='idiomauser',
            name='idioma_sabe',
            field=models.ForeignKey(db_column='idioma_sabe', to='registro.TablaIdioma'),
        ),
    ]
