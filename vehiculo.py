class Vehiculo:
    # DISTANCIA_BASE = 12
    FACTOR_EMISION_GASOLINA = 2.196
    FACTOR_EMISION_DIESEL = 2.471

    def __init__(self, placa, marca, modelo, color, combustible, tanque, kilometraje, AC):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.combustible = combustible
        self.tanque = tanque
        self.kilometraje = kilometraje
        self.__AC = AC
        self.encendido = False
        self.litros_consumidos = 0

    # def encender(self):
    #     self.encendido = True
    #     print("Encendiendo...")

    # def apagar(self):
    #     self.encendido = False
    #     print("Apagando...")

    def tocar_bocina(self):
        print("Bip bip bip")

    def frenar(self):
        print("Frenando...")

    def obtener_litros_tanque(self):
        return self.tanque

    def obtener_descripcion(self):
        formato_descripcion = "Placa: {}, Marca: {}, Modelo: {}, Color: {}, Combustible: {}, Kilometraje: {}, Tanque: {}, ¿Tiene AC? {}"
        descripcion = formato_descripcion.format(self.placa, self.marca, self.modelo, self.color,
                                                 self.combustible, self.kilometraje, self.tanque, self.traducir_respuesta(self.__AC))
        return descripcion

    def __str__(self):
        formato_descripcion = "Placa: {}, Marca: {}, Modelo: {}, Color: {}, Combustible: {}, Kilometraje: {}, Tanque: {}, ¿Tiene AC? {}"
        descripcion = formato_descripcion.format(self.placa, self.marca, self.modelo, self.color,
                                                 self.combustible, self.kilometraje, self.tanque, self.traducir_respuesta(self.__AC))
        return descripcion

    def traducir_respuesta(self, valor):
        if valor:
            return "Si"
        return "No"

    def cargar_combustible(self, litros):
        self.tanque += litros
        print("Cargando combustible...")

    # def recorrer_distancia2(self, distancia):
    #     if self.encendido:
    #         if distancia < (self.DISTANCIA_BASE * self.tanque):
    #             total_litros = round(distancia / self.DISTANCIA_BASE, 2)
    #             self.tanque -= total_litros
    #             self.kilometraje += distancia
    #             self.litros_consumidos += total_litros
    #             print("Recorriendo distancia...")
    #         else:
    #             print("No hay combustible suficiente")
    #     else:
    #         print("El vehiculo esta apagado")

    def recorrer_distancia(self, distancia):
        variante = self.obtener_variante_consumo_combustible()
        if self.motor.esta_encendido():
            if distancia < (variante * self.tanque):
                total_litros = round(distancia / variante, 2)
                self.tanque -= total_litros
                self.kilometraje += distancia
                self.litros_consumidos += total_litros
                print("Recorriendo distancia...")
            else:
                print("No hay combustible suficiente")
        else:
            print("El vehiculo esta apagado")

    # def hay_combustible2(self, distancia):
    #     if not distancia < (self.DISTANCIA_BASE * self.tanque):
    #         return False
    #     return True

    def hay_combustible(self, distancia):
        variante = self.obtener_variante_consumo_combustible()
        if not distancia < (variante * self.tanque):
            return False
        return True

    def calcular_C02(self):
        if self.combustible == "Gasolina":
            return self.litros_consumidos * self.FACTOR_EMISION_GASOLINA
        else:
            return self.litros_consumidos * self.FACTOR_EMISION_DIESEL

    def obtener_informe(self):
        informe = "\n--------------------------------------------------"
        informe += "\nINFORME FINAL - EMISION DE DIOXIDO DE CARBONO"
        informe += "\n--------------------------------------------------"
        informe += "\nUd. esta conduciendo un vehiculo marca: {}, modelo: {}, color: {}, placa: {}".format(
            self.marca, self.modelo, self.color, self.placa)
        informe += "\nHa recorrido un total de {} KM de distancia".format(
            self.kilometraje)
        informe += "\nHa consumido un total de {} litros de {}".format(
            self.litros_consumidos, self.combustible)
        informe += "\nEn su tanque tiene {} litros de {}".format(
            round(self.tanque, 2), self.combustible)
        informe += "\nSe emitio a la atmosfera un total de {} kg de C02".format(
            round(self.calcular_C02(), 2))
        return informe

    def poner_motor(self, motor):
        self.motor = motor

    def obtener_variante_consumo_combustible(self):
        cilindrada = self.motor.obtener_cilindrada()
        if cilindrada == 1000:
            return 12
        elif cilindrada == 2000:
            return 10
        else:
            return 8
