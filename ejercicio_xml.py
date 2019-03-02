from lxml import etree
doc = etree.parse('colegios-lorca.xml')

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
        def colegio(doc):
            lista = doc.xpath('''//Localizacion[not(Pedania='Lorca')]/../Centro/text() |
            //Localizacion[not(Pedania='Lorca')]/../Contacto/Web/text() |
            //Localizacion[not(Pedania='Lorca')]/../Contacto/Telefono/text() |
            //Localizacion[not(Pedania='Lorca')]/../Contacto/Email/text()
            //Localizacion[not(Pedania='Lorca')]/../Contacto/Fax/text()
            ''')

            return lista

        for col in colegio(doc):
            print(col)


    elif opcion==2:

    #Cuenta los colegios que no tiene página web y muestra su nombre

        def colegio(doc):
            lista = doc.xpath("//Contacto[not(Web)]/../Centro/text()")
            return lista

        for col in colegio(doc):
            print(col)
        print ("")

    elif opcion==3:

    #Pide una pedania y muestra el nombre de los colegios y su dirección

        def poblacion(doc):
            pueblo=input("Dime una pedania:").capitalize()
            calle = doc.xpath('//Localizacion[Pedania="%s"]/./Direccion/text()'%pueblo)
            centro = doc.xpath('//Centro[//Localizacion[Pedania="%s"]]/text()'%pueblo)
            return zip(calle,centro)

        for calle,centros in poblacion(doc):
            print (centros," - ",calle)
        print ("")

    #Introduce un número de teléfono y muestra el Centro al que pertenece

    elif opcion==4:
        def telefono(telefono,doc):
            centro =  doc.xpath('//Contacto[Telefono="%s"]/../Centro/text()'%telefono)
            return centro

        tlf=input("Dime número de telefono de un centro:")

        print (telefono(tlf,doc))

    #Introduce nombre del Instituto y te da un enlace a OpenStreetMap de su localización

    elif opcion==5:
        def localizar(doc):
            centro=input("Dime el nombre del centro para obtener su cordenada:").upper()
            latitud = str(doc.xpath('//colegio_lorca[Centro="%s"]/Localizacion/Coordenadas/Latitud/text()'%centro))
            longitud = str(doc.xpath('//colegio_lorca[Centro="%s"]/Localizacion/Coordenadas/Longitud/text()'%centro))

            latitud2 = latitud.replace("[","").replace("]","").replace("'","")
            longitud2 = longitud.replace("[","").replace("]","").replace("'","")
            print (latitud2,latitud2)
            localizador="http://www.openstreetmap.org/#map=16/%s/%s"%(latitud2,longitud2)
            return localizador

        print (localizar(doc))



    elif opcion == 0:
        break;
    else:
        print ("Esa opcion no existe")
