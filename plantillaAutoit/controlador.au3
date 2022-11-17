; Sección de importación librerias
#include "modelo.au3"
#include "funcionCorreo.au3"

; Descripción: Método responsable de conectar con el módelo.
Func consultarPacienteControlador($documento)
   $datos = consultarPacienteModelo($documento)
   Local $registro
   $var = 1
   While _SQL_FetchData($datos, $registro) = $SQL_OK
	  MsgBox(0, "Paciente", $documento & " - " & $registro[0])
   WEnd
EndFunc

; Descripción: Método responsable de enviar un correo electrónico.
Func enviarCorreoElectronico()
   $correoPara = "jospina@clinicasomer.com"
   $asunto = "Prueba de envío de correo"
   $mensaje = "Mensaje de envío de correo electrónico"
   $adjuntos = ""
   $correoCopia = "andres.ospina1807@gmail.com"
   $correoCopiaOculta = ""
   $importancia = "Normal"   ; --> "High", "Normal", "Low"
   envioCorreo($correoPara, $asunto, $mensaje, $adjuntos, $correoCopia, $correoCopiaOculta, $importancia)
EndFunc