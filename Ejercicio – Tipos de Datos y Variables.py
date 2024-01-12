print ("""Selecciona la operacion que deseas realizar: 
      suma
      resta
      multiplicacion
      division
      potencia
      """)

opcion = input("Que operacion deseas realizar: ")

num1 = float(input("Ingresa el numero 1: "))
num2 = float(input("Ingresa el numero 2: "))

if opcion == 'suma':
    print(f"La suma de los numeros {num1} y {num2} es {num1 + num2}")
elif opcion == 'resta':
    print(f"La resta de los numeros {num1} y {num2} es: {num1 -num2}")
elif opcion == 'multiplicacion':
    print(f"La Multiplicacion de los numeros {num1} y {num2} es {num1 * num2}")
elif opcion == 'division':
    print(f"La Division de los numeros {num1} y {num2} es: {num1/num2}")
elif opcion == 'potencia':
    print(f"El numero {num1} elevado a la {num2} es {num1**num2}")
else:
    print("No ingresaste una opcion valida")