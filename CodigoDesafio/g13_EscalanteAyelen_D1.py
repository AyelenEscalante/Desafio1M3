def votar(nombre,edad):
    if edad >= 16:
        return nombre+" "+"puede votar" 
    else:
        return nombre+" "+"debe esperar para votar" 
el_nombre= input ("Ingrese su nombre y apellido por favor:") 
la_edad= int ( input ("Ingrese su edad por favor:"))
if la_edad>=16:
    print(el_nombre+" "+"puede votar")
else:
    print(el_nombre+" "+"debe esperar para votar")
    

