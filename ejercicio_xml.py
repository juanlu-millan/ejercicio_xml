from lxml import etree
doc = etree.parse('colegios-lorca.xml')

from funciones_xml import contacto
from funciones_xml import colegio
from funciones_xml import poblacion
from funciones_xml import telefono
from funciones_xml import localizar

while (True):
    print('''
    Elige una opcion:
    1. Lista conctatos de cada colegio que no pertenece a la pedania de lorca
    2. Cuenta los colegios que no tiene página web y muestra su nombre
    3. Pide una pedania y muestra el nombre de los colegios y su dirección
    4. Introduce un número de teléfono y muestra el Centro al que pertenece
    5. URL de Centro
    0-Salir''')
    opcion=int(input("Opcion: "))

    if opcion==1:
    #Lista conctatos de cada colegio que no pertenece a la pedania de lorca
        for col in contacto(doc):
            print(col)


    elif opcion==2:

    #Cuenta los colegios que no tiene página web y muestra su nombre
        for col in colegio(doc):
            print(col)
        print ("")

    elif opcion==3:

    #Pide una pedania y muestra el nombre de los colegios y su dirección

        pueblo=input("Dime una pedania:").capitalize()

        for calle,centros in poblacion(pueblo,doc):
            print (centros," - ",calle)
        print ("")



    elif opcion==4:
    #Introduce un número de teléfono y muestra el Centro al que pertenece

        tlf=input("Dime número de telefono de un centro:")

        print (telefono(tlf,doc))



    elif opcion==5:
    #Introduce nombre del Instituto y te da un enlace a OpenStreetMap de su localización

        colegio=input("Dime el nombre del centro para obtener su cordenada:").upper()

        print (localizar(colegio,doc))


    elif opcion == 0:
        break;
    else:
        print ("Esa opcion no existe")
