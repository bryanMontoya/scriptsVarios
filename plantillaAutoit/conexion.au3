; Descripción: Método responsable de conectar con la base de datos.
Func conectar($sql)
   $ADODBHandle = _SQL_Startup()
   If $ADODBHandle == $SQL_ERROR Then
	  ; TODO: Controlar el error para crear arbol de decisiones.
	  MsgBox(0 & 16 & 262144, "Error", _SQL_GetErrMsg())
   EndIf
   $con = _SQL_Connect($ADODBHandle, $SERVIDOR_BD, $BASE_DATOS, $USUARIO_BD, $CONTRASENA_BD)
   $datos = _SQL_Execute(-1, $sql)
   _SQL_Close($ADODBHandle = -1)
   Return $datos
EndFunc