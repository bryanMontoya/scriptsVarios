# Descripción: Archivo que contiene los parámetros generales del aplicativo


#****************** Conexión a la base de datos *******************
#******************************************************************

# Ambiente de DESARROLLO
# Empresa SOMER
ruta = '//192.168.30.35/Conexiones$/desarrollo-somer.txt'

# Ambiente de DESARROLLO
# Empresa INCARE
# ruta = '//192.168.30.35/Conexiones$/desarrollo-incare.txt'

# Ambiente de PRODUCCIÓN
# Empresa SOMER
#ruta = '//192.168.30.35/Conexiones$/produccion-somer.txt'

# Ambiente de PRODUCCIÓN
# Empresa INCARE
# ruta = '//192.168.30.35/Conexiones$/produccion-incare.txt'

#******************************************************************
#******************************************************************

variables = []
with open(ruta,'r') as archivo:
	lineas = archivo.readlines()
	for linea in lineas:
		variables.append(linea.strip('\n'))
SERVIDOR_BD = variables[0]
USUARIO_BD = variables[1]
CONTRASENA_BD = variables[2]
BASE_DATOS = variables[3]
BD_DINAMICA = variables[4]
BD_RPA = variables[5]
BD_GESTOR = variables[6]


#****************** Instalar librería pip install pymssql *******************