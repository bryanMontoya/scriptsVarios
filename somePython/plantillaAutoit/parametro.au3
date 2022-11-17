; Descripción: Archivo que contiene los parámetros generales del aplicativo.

;****************** Conexión a la base de datos *******************
;******************************************************************

; Ambiente de DESARROLLO
; Empresa SOMER
$archivo = "\\192.168.30.35\Conexiones$\desarrollo-somer.txt"

; Ambiente de DESARROLLO
; Empresa INCARE
;~ $archivo = "\\192.168.30.35\Conexiones$\desarrollo-incare.txt"

; Ambiente de PRODUCCIÓN
; Empresa SOMER
;~ $archivo = "\\192.168.30.35\Conexiones$\produccion-somer.txt"

; Ambiente de PRODUCCIÓN
; Empresa INCARE
;~ $archivo = "\\192.168.30.35\Conexiones$\produccion-incare.txt"

;******************************************************************
;******************************************************************

FileOpen($archivo, 0)
Local $variables[7]
For $i = 1 to _FileCountLines($archivo)
    $linea = FileReadLine($archivo, $i)
    $variables[$i - 1] = $linea
Next
FileClose($archivo)
Const $SERVIDOR_BD = $variables[0]
Const $USUARIO_BD = $variables[1]
Const $CONTRASENA_BD = $variables[2]
Const $BASE_DATOS = $variables[3]
Const $BD_DINAMICA = $variables[4]
Const $BD_RPA = $variables[5]
Const $BD_GESTOR = $variables[6]