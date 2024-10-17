print("")
print("Alfaro Ibarra Sheccid, 3w, 1171. Divisas")
#Colocamos el diccionario 
dicciodivisa={ "Euro":"€", "Dollar":"$","Yen":"¥"
    }
#Preguntamos al usuario sobre la divisa
divisa=(input("Coloca la divisa aqui:"))
#Utilizamos if para dar una respuesta al usuario
if divisa in dicciodivisa:
    print("La divisa se encuentra en nuestros datos.")
    print(dicciodivisa[divisa])
else:
    print("La divisa no se encuentra en nuestros datos.")
    