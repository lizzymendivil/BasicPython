class Motor:
    def __init__(self, nro_serie, cilindrada):
        self.nro_serie = nro_serie
        self.cilindrada = cilindrada
        self.encendido = False

    def obtener_cilindrada(self):
        return self.cilindrada

    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False

    def esta_encendido(self):
        return self.encendido
