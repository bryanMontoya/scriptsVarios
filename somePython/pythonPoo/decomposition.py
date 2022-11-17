class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.__estado = "En resposo" #Private
        self._motor = Motor(cilindros = 4)
    
    def acelerar(self, tipo = "despacio"):
        if tipo == "rapida":
            self._motor.inyectaGasolina(10)
        else:
            self._motor.inyectaGasolina(3)
        
        self.__estado = "En movimiento"
    
    

class Motor:
    def __init__(self, cilindros, tipo = "Gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyectaGasolina(self, cantidad):
        pass
