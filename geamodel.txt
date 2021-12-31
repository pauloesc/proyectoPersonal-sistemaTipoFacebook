# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class CookieHash(models.Model):
    sesion_llave = models.TextField()
    usuario = models.TextField()
    expira_fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cookie_hash'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class IdiomaUser(models.Model):
    habla = models.ForeignKey('TablaUsuario')
    idioma_sabe = models.ForeignKey('TablaIdioma', db_column='idioma_sabe')

    class Meta:
        managed = False
        db_table = 'idioma_user'


class RegistroDocument(models.Model):
    filename = models.CharField(max_length=100)
    docfile = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'registro_document'


class TablaIdioma(models.Model):
    idioma = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tabla_idioma'


class TablaLenguaje(models.Model):
    lenguaje = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tabla_lenguaje'


class TablaNivel(models.Model):
    nivel = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tabla_nivel'


class TablaPregunta(models.Model):
    pregunta_contenido = models.TextField()
    pregunta_fecha = models.DateField()
    pregunta_id = models.AutoField(primary_key=True)
    pregunta_idioma = models.ForeignKey(TablaIdioma, db_column='pregunta_idioma')
    pregunta_lenguaje = models.ForeignKey(TablaLenguaje, db_column='pregunta_lenguaje')
    pregunta_nivel = models.ForeignKey(TablaNivel, db_column='pregunta_nivel')
    pregunta_user = models.ForeignKey('TablaUsuario', db_column='pregunta_user')

    class Meta:
        managed = False
        db_table = 'tabla_pregunta'


class TablaRespuesta(models.Model):
    respuesta_contenido = models.TextField()
    respuesta_fecha = models.DateField()
    votos = models.IntegerField(blank=True, null=True)
    respuesta = models.ForeignKey(TablaPregunta)
    respuesta_username = models.ForeignKey('TablaUsuario', db_column='respuesta_username')

    class Meta:
        managed = False
        db_table = 'tabla_respuesta'


class TablaUsuario(models.Model):
    username = models.TextField(primary_key=True)
    nombre = models.TextField()
    apellido = models.TextField()
    correo = models.TextField()
    passw = models.TextField()

    class Meta:
        managed = False
        db_table = 'tabla_usuario'


class UsuarioLenguajeNivel(models.Model):
    user_lenguaje = models.ForeignKey(TablaLenguaje, db_column='user_lenguaje')
    user_nivel = models.ForeignKey(TablaNivel, db_column='user_nivel')
    user_sabe = models.ForeignKey(TablaUsuario, db_column='user_sabe')

    class Meta:
        managed = False
        db_table = 'usuario_lenguaje_nivel'
