; Sección de importación librerias
#include "conexion.au3"

;********************** Seleccion de la base de datos solicitada **********************
;**************************************************************************************
; $BD_DINAMICA
; $BD_SOMER
; $BD_GESTOR
;**************************************************************************************
;**************************************************************************************

; Descripción: Método responsable de conectar con la base de datos.
Func consultarPacienteModelo($documento)
   $documento = "'" & $documento & "'"
   $sql = "SELECT GPANOMCOM AS PACIENTE"
   $sql = $sql & " FROM " & $BD_DINAMICA & ".GENPACIEN INNER JOIN " & $BD_GESTOR & ".GC_ONCO_RADIO_TRATAMIENTO ON GENPACIEN.PACNUMDOC = GC_ONCO_RADIO_TRATAMIENTO.PACNUMDOC"
   $sql = $sql & " WHERE GENPACIEN.PACNUMDOC = " & $documento
   $datos = conectar($sql)
   Return $datos
EndFunc