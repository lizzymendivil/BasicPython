from vehiculo import Vehiculo
from simulador import Simulador
from motor import Motor

coche1 = Vehiculo("3797IYH", "Suzuki", "2015", "Azul", "Gasolina", 1, 0, False)
coche2 = Vehiculo("4578POO", "Suzuki", "2015", "Azul", "Gasolina", 1, 0, False)

motor1 = Motor("454545", 1000)
motor2 = Motor("454545", 2000)

coche1.poner_motor(motor1)
coche2.poner_motor(motor2)

lista = [coche1, coche2]
simulador = Simulador(lista)
simulador.iniciar_simulacion(5)
