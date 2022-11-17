class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia(self, otraCoordenada):
        return ((self.x - otraCoordenada.x)**2 + (self.y - otraCoordenada.y)**2)**(1/2)

if __name__ == '__main__':
    coord1 = Coordenada(3, 20)
    coord2 = Coordenada(4, -5)

    print(coord1.distancia(coord2))
    print(isinstance(3, Coordenada)) #Es instancia de Coordenada.
    #print(isinstance(3, int))