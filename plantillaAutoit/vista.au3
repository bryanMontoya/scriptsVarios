; Sección de importación librerias
#include <Array.au3>
#include <WinAPI.au3>
#include <WindowsConstants.au3>
#Include <file.au3>
#include "lib\_SQL.au3"
#include "parametro.au3"
#include "controlador.au3"

; Descripción del método: Método responsable de ejecutar las funciones del aplicativo.
Func menu()
   ; Llamada al método consultar paciente.
   $documento = "15437709"
   consultarPacienteControlador($documento)

   ; Llamada al método envío correo.
   ;~ enviarCorreoElectronico();
EndFunc

; Llamado al método principal.
menu()