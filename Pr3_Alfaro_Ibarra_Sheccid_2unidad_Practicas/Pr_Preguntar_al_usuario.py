print("")
print("ALfaro Ibarra Sheccid, 3w, 1171. Pregunta al usuario.")
#Preguntar al usuario
nm=input("Ingresa el nombre:")
ed=input("Ingresa la edad:")
drc=input("Ingrese la direccion:")
tlf=input("Ingrese el numero de telefono:")
#Definir el diccionario
dicdeinf={
    "Nombre" : nm,
    "Edad" : ed,
    "Direccion" : drc,
    "Telefono" : tlf
}
#Proporcionar la informacion que ha puesto el usuario en pantalla
print("")
print("Bievenido, usted es:")
print(dicdeinf["Nombre"])
print("Tiene la edad de:")
print(dicdeinf["Edad"])
print("La direccion proporcionada es:")
print(dicdeinf["Direccion"])
print("El telefono que ha puesto es")
print(dicdeinf["Telefono"])

