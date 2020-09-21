
# Hacer un programa que calcule el precio a pagar de cada cliente de una panaderia
# y la cantidad de kg vendidos en el dia.



#Las primeras mejoras que realizare al programa seran:
#Cambio masivo de nombre en las variables para un mejor entendimiento de cada una
#Agregare antes de entrar al WHILE dos ingresos para que el usuario pueda poner el precio al pan que el quiera cobrar en el dia, ya que ahora se encuentra de forma predeterminada por el programador
#Borrare variables declaradas que no son necesarias

#Las segundad mejoras que realizare al programa seran:
#Agregar mas funciones al programa como una lista nueva y el uso de un acumulador para mostrar mas datos en la salida del programa
#Cambio en el nombre de la variable inicial del "while", que mejorara el uso del programa al usuario

#Tambien cambio el valor inicial que tendra la primer variable
PanaderiaAbierta = "S"
CantPanComun = 0
CantPanSalv = 0
KGPan = []
Cliente = 0
#Creare otra lista para calcular el total de dinero recaudado por la panaderia en el dia
TotalRecaudado = []

#Borro los "int" puestos en los dos def ya que no son necesarios
def CalculoPanComun (PrecioPanComun,CantPanComun):
    CalculoPanComun = CantPanComun * PrecioPanComun
    return CalculoPanComun

def CalculoPanSalv (PrecioPanSalv,CantPanSalv):
    CalculoPanSalv = CantPanSalv * PrecioPanSalv
    return CalculoPanSalv

def TotalCliente (TotalPanComun,TotalPanSalvado):
    TotalCliente = TotalPanComun + TotalPanSalvado
    #Agregare la lista creada en este def para guardar el total de cada cliente
    TotalRecaudado.append(TotalCliente)
    return TotalCliente

#Aca vemos una de las mejoras que realice, el pedido del precio del pan al usuario
PrecioPanComun = float(input("Ingrese el valor que tendra el pan comun el dia de hoy: "))
PrecioPanSalv = float(input("Ingrese el valor que tendra el pan de salvado el dia de hoy: "))

#Cambiare el valor que debera tener PanaderiaAbierta a un valor de una sola letra, de este modo el usuario solo debera tocar una tecla para ingresar
while PanaderiaAbierta == "S":
    #Las mejoras que realizare en esta segunda parte seran cambiar estos "int" por "float", ya que el pan se puede vender no solo en numeros enteros
    CantPanComun = float(input("Ingrese la cantidad de Kg de pan comun de esta compra: "))
    CantPanSalv = float(input("Ingrese la cantidad de Kg de pan de salvado de esta compra: "))
    TotalPanComun = CalculoPanComun(PrecioPanComun,CantPanComun)
    TotalPanSalvado = CalculoPanSalv(PrecioPanSalv,CantPanSalv)
    KGPan.append(CantPanComun+CantPanSalv)
    print("El monto de este cliente es de: $", TotalCliente(TotalPanComun,TotalPanSalvado))
    #El programador original, dejo este acumulador sin ningun uso, para no sacarlo, decidi cambiarle el nombre y de este modo poder calcular la cantidad de clientes que tuvo la panaderia
    Cliente = Cliente + 1
    #Del mismo modo cambio la respuesta que espero del usuario en esta pregunta
    PanaderiaAbierta = str(input("Desea ingresar otra compra? S/N"))
    PanaderiaAbierta = PanaderiaAbierta.upper()

#Borro y cambio el metodo utilizado para la suma total de KG que utilizo el programador original, la cambio por una mas corta y sencilla
#Cambio el "for" por el metodo "sum" de lista
TotalKGDia = sum(KGPan)

#En el siguiente print mostrare la cantidad de clientes que tuvo la panaderia usando el acumulador "Cliente"
print("La panaderia tuvo un total de",Cliente,"cliente(s) el dia de hoy")
print("El total de Kg vendidos fue: ", TotalKGDia,"KG")
#Agregare un print donde se sumara la lista y mostrara el total recaudado
print("El total recaudado de la panaderia en el dia de hoy fue de: $",sum(TotalRecaudado))














