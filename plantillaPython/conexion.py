# Sección de importación librerias
import pymssql
import parametro

# Descripción: Método responsable de conectar con la base de datos.
def conectar():
    conn = pymssql.connect(parametro.SERVIDOR_BD, parametro.USUARIO_BD, parametro.CONTRASENA_BD, parametro.BASE_DATOS)
    return conn