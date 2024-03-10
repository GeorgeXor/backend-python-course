print("Carrito de Comrpas".center(100,"-"))

menu = {
    1 : "PAN" ,
    2 : "CAFE" ,
    3 : "AZUCAR" ,
    4 : "LECHE" ,
    5 : "GALLETAS" ,
    6 : "CARNE" ,
    7 : "PESCADO" ,
    8 : "SOPA"
}

def mostrar_menu(menu:dict):
    for key , values in menu.items():
        print(f"Id_Producto: {key} -- Desc_Producto: {values}")
        

def get_id_menu(menu:dict):
    return list(menu.keys())

def crea_carrito(id_productos:list):
    
    val  = 1
    carrito = []
    while val == 1 :

        id_prod = int(input("Ingresa el Id del producto que deseas llevar: "))
        if id_prod in id_productos:
            cant_prod = int(input("Ingresa la Cantidad que vas a llevar del Producto: "))
            if cant_prod > 0:
                orden = [id_prod,cant_prod]
                carrito.append(orden)
            else:
                print("La cantidad debe ser mayor a cero")
                break
            
        else:
            print("El Id de Producto ingresado no esta dentro del Menu")
            break
        
        orden = input("Desea agregar mas productos a su carrito? [Y/N]")
        
        if orden == 'N': 
            break
        elif orden == 'Y':
            continue
        else:
            print("Opcion no valida, favor de ingresar Y o N")

    return carrito

def mostrar_carrito(carrito,menu):
    
    for i in range(len(carrito)):
        print(f' Producto {i+1} : {menu[carrito[i][0]]} - Cantidad: {carrito[i][1]}')

mostrar_menu(menu)
id_productos = get_id_menu(menu)
carrito = crea_carrito(id_productos)
mostrar_carrito(carrito,menu)