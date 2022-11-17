class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura = "caliente"):
        self._llenarTanqueDeAgua(temperatura)
        self._agregarJabon()
        self._lavar()
        self._centrifugar()

    def _llenarTanqueDeAgua(self, temperatura):
        print(f"Llenando el tanque con agua {temperatura}")
    
    def _agregarJabon(self):
        print("Añadiendo Jabon")
    
    def _lavar(self):
        print("Lavando la ropa")
    
    def _centrifugar(self):
        print("Centrifugando la ropa")
    
if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()