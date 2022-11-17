class CasillaDeVotacion():
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self.__region = None
    
    #Getter
    @property
    def region(self):
        return self._region

    #Setter
    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no es valida en {self.__pais}')
'''
    #Deleter
    @region.deleter
    def region(self):
        print('Borrando region')
        del self._region      '''
    

casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos'])
casilla.region = 'Ciudad de Mexico'
print(casilla.region)
print(casilla.region)
