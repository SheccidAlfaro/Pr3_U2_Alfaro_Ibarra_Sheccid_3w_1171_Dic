print("")
print("Alfaro Ibarra Sheccid, 3w, 1171. Precios de frutas.")
#DEfinir el diccionario
dicdefrut={
    "Mango" : 10,
    "Kiwi" : 8,
    "Mandarina" : 5,
    "Papaya" : 12,
    "Durazno" : 7
}
#Preguntar al usuario
fruta=input("Ingrese aqui la fruta que desee comprar:")
kgdefru=float(input("Ingrese la cantidad de kilogramos que va a comprar."))
#Utilizar if para  verificar si la fruta existe en el diccionario

if fruta in dicdefrut:
    prf=dicdefrut[fruta]* kgdefru
    print("El precio de la fruta es: ", prf)
else:
    print("La fruta no se encuentra en la lista de precios")
#Mostrar el precio  de la fruta, como de lo que pasa si la fruta no  existe en el diccionario.

