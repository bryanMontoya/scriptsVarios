# Sección de importación librerias
import controlador 

# Descripción del método: Método responsable de ejecutar las funciones del aplicativo.
def menu():
   # Llamada al método consultar paciente.
   documento = "12345"
   #documento = "15437709"
   #documento = "39440450"
   controlador.consultarPacienteControlador(documento)

# Llamado al método principal.
menu()