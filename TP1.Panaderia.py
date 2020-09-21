# Hacer un programa que calcule el precio a pagar de cada cliente de una panaderia
# y la cantidad de kg vendidos en el dÃ­a.



#Las primeras mejoras que realizare al programa seran:
#Cambio masivo de nombre en las variables para un mejor entendimiento de cada una
#Agregare antes de entrar al WHILE dos ingresos para que el usuario pueda poner el precio al pan que el quiera cobrar en el dia, ya que ahora se encuentra de forma predeterminada por el programador
#Borrare variables declaradas que no son necesarias
PanaderiaAbierta = "SI"
CantPanComun = 0
CantPanSalv = 0
KGPan = []
Cliente = 0

#Borro los "int" puestos en los dos def ya que no son necesarios
def CalculoPanComun (PrecioPanComun,CantPanComun):
    CalculoPanComun = CantPanComun * PrecioPanComun
    return CalculoPanComun

def CalculoPanSalv (PrecioPanSalv,CantPanSalv):
    CalculoPanSalv = CantPanSalv * PrecioPanSalv
    return CalculoPanSalv

def TotalCliente (TotalPanComun,TotalPanSalvado):
    TotalCliente = TotalPanComun + TotalPanSalvado
    return TotalCliente

#Aca vemos una de las mejoras que realice, el pedido del precio del pan al usuario
PrecioPanComun = float(input("Ingrese el valor que tendra el pan comun el dia de hoy: "))
PrecioPanSalv = float(input("Ingrese el valor que tendra el pan de salvado el dia de hoy: "))

while PanaderiaAbierta == "SI":
    CantPanComun = int(input("Ingrese la cantidad de Kg de pan comun de esta compra: "))
    CantPanSalv = int(input("Ingrese la cantidad de Kg de pan de salvado de esta compra: "))
    TotalPanComun = CalculoPanComun(PrecioPanComun,CantPanComun)
    TotalPanSalvado = CalculoPanSalv(PrecioPanSalv,CantPanSalv)
    KGPan.append(CantPanComun+CantPanSalv)
    print("El monto de este cliente es de: $", TotalCliente(TotalPanComun,TotalPanSalvado))
    Cliente = Cliente + 1
    PanaderiaAbierta = str(input("Desea ingresar otra compra? Si/No"))
    PanaderiaAbierta = PanaderiaAbierta.upper()

#Borro y cambio el metodo utilizado para la suma total de KG que utilizo el programador original, la cambio por una mas corta y sencilla
#Cambio el "for" por el metodo "sum" de lista
TotalKGDia = sum(KGPan)

print("El total de Kg vendidos fue: ", TotalKGDia)














