# Sección de importación librerias
import modelo

# Descripción: Método responsable de conectar con el módelo.
def consultarPacienteControlador(documento):
    datos = modelo.consultarPacienteModelo(documento)
    listaRegistros = []
    for registro in datos.fetchall():
        listaRegistros.append(registro)
        print(registro)