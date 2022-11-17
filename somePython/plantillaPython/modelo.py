# Sección de importación librerias
import conexion
import parametro

#********************** Seleccion de la base de datos solicitada **********************
#**************************************************************************************
# parametro.BD_DINAMICA
# parametro.BD_RPA
# parametro.BD_GESTOR
#**************************************************************************************
#**************************************************************************************

# Descripción: Método responsable de conectar con la base de datos.
def consultarPacienteModelo(documento):
    documento = "'" + str(documento) + "'"
    sql = "SELECT GPANOMCOM AS PACIENTE"
    sql = sql + " FROM " + parametro.BD_DINAMICA + ".GENPACIEN INNER JOIN " + parametro.BD_GESTOR + ".GC_ONCO_RADIO_TRATAMIENTO ON GENPACIEN.PACNUMDOC = GC_ONCO_RADIO_TRATAMIENTO.PACNUMDOC"
    sql = sql + " WHERE GENPACIEN.PACNUMDOC = " + documento
    conn = conexion.conectar()
    datos = conn.cursor()
    sql = "SELECT GPANOMCOM AS PACIENTE FROM " + parametro.BD_DINAMICA + ".GENPACIEN WHERE GENPACIEN.PACNUMDOC = " + documento
    datos.execute(sql)
    # Usar solo en insert y update:
    # conn.commit()
    # conn.close()
    return datos