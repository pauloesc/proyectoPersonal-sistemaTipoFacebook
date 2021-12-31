from __future__ import unicode_literals
from django.db import models

class IdiomaUser(models.Model):
    habla = models.ForeignKey('TablaUsuario')
    idioma_sabe = models.ForeignKey('TablaIdioma', db_column='idioma_sabe')

    class Meta:
        managed = True
        db_table = 'idioma_user'

class TablaIdioma(models.Model):
    idioma = models.TextField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'tabla_idioma'

class TablaLenguaje(models.Model):
    lenguaje = models.TextField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'tabla_lenguaje'

class TablaNivel(models.Model):
    nivel = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'tabla_nivel'

class TablaPregunta(models.Model):
    pregunta_contenido = models.TextField()
    pregunta_fecha = models.DateField()
    pregunta_id = models.AutoField(primary_key=True)
    pregunta_user = models.ForeignKey('TablaUsuario', db_column='pregunta_user')
    pregunta_lenguaje = models.ForeignKey(TablaLenguaje, db_column='pregunta_lenguaje')
    pregunta_nivel = models.ForeignKey(TablaNivel, db_column='pregunta_nivel')
    pregunta_idioma = models.ForeignKey(TablaIdioma, db_column='pregunta_idioma')

    class Meta:
        managed = True
        db_table = 'tabla_pregunta'

class TablaRespuesta(models.Model):
    respuesta_contenido = models.TextField()
    respuesta_fecha = models.DateField()
    votos = models.IntegerField(blank=True, null=True)
    respuesta_username = models.ForeignKey('TablaUsuario', db_column='respuesta_username')
    respuesta = models.ForeignKey(TablaPregunta)

    class Meta:
        managed = True
        db_table = 'tabla_respuesta'

class TablaUsuario(models.Model):
    username = models.TextField(primary_key=True)
    nombre = models.TextField()
    apellido = models.TextField()
    correo = models.TextField()
    passw = models.TextField()

    class Meta:
        managed = True
        db_table = 'tabla_usuario'

class UsuarioLenguajeNivel(models.Model):
    user_sabe = models.ForeignKey(TablaUsuario, db_column='user_sabe')
    user_nivel = models.ForeignKey(TablaNivel, db_column='user_nivel')
    user_lenguaje = models.ForeignKey(TablaLenguaje, db_column='user_lenguaje')

    class Meta:
        managed = True
        db_table = 'usuario_lenguaje_nivel'

class Document(models.Model):
	filename = models.CharField(max_length=100)
	docfile = models.FileField(upload_to='documents')