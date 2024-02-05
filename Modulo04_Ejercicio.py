numlist = [1,2,3,4,5] #Ejemplo1: Lista con 5 numeros
numtupla = (1,3,5,7,9) #Ejemplo2: Tupla con 5 numeros

operaciones = ['Suma','Resta','Multiplicacion','Division']
valores_permitidos = (list,tuple,dict)

def menu_inicio():
    operacion = input("Selecciona la Operacion que deseas realizar: \nSuma\nResta\nMultiplicacion\nDivision \n Que operacion quieres realizar:  ")
    return operacion

def valida_valores(obj):
    if type(obj) in valores_permitidos:
        if len(obj) >= 5:
            return obj
        else:
            return 101#El codigo 101 significa que la lista no contiene los elementos Necesarios
    else:
        return 102#El Codigo 102 significa que el objeto ingresado no es una Lista , Tupla o Diccionario

def valida_operacion(operacion):
    if operacion in operaciones:
        return 1 
    else:
        return 103#El codigo 103 significa que la operacion seleccionada no es correcta
        

def operaciones_basicas (valor,operacion):
    resultado = 0    
    if operacion == 'Suma':
        for i in valor: 
            resultado = resultado + i
        print(f"La suma de los valores {valor} es {resultado} ")
    elif operacion == 'Resta':
        for i in valor: 
            resultado = resultado - i
        print(f"La resta de los valores {valor} es {resultado} ")
    elif operacion == 'Multiplicacion':
        resultado = 1
        for i in valor: 
            resultado = resultado * i
        print(f"La multiplicacion de los valores {valor} es {resultado} ")
    elif operacion == 'Division':
        resultado = 1
        for i in valor: 
            resultado = 1
            resultado = resultado / i
        print(f"La division de los valores {valor} es {resultado} ")

operacion = menu_inicio()

if valida_operacion(operacion) == 1:
    res = valida_valores(numlist)
    if res == 101:
        print("")
    elif res == 102:
        print("")
    else:
        operaciones_basicas(numlist,operacion)
