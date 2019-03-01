from lxml import etree
doc = etree.parse('colegios-lorca.xml')

while (True):
    print('''
    Elige una opcion:
    1. Número total de postales
    2. Número total de postales por Estado
    3. URL de ciudad
    0-Salir''')
    opcion=int(input("Opcion: "))

    if opcion==1:

        #Lista conctatos de cada colegio que no pertenece a la pedania de lorca
        def colegio(doc):

            if doc.xpath(//Localizacion[not(Pedania='Lorca')]/text()):
                lista = doc.xpath("//Web/text() | //Email/text() | //Telefono/text() | //Fax/text() | //Localizacion[not(Pedania='Lorca')]")

            return lista

        for col in colegio(doc):
            print(col)

    if opcion==2:

        #Cuenta los colegios que no tiene página web y muestra su nombre

        def colegio(doc):
            lista = doc.xpath("//Contacto[not(Web)]/../Centro/text()")
            return lista

        for col in colegio(doc):
            print(col)

    if opcion==3:

        #Pide una pedania y muestra el nombre de los colegios y su dirección

        def poblacion(doc):
            pueblo=input("Dime una pedania:").capitalize()
            calle = doc.xpath('//Localizacion[Pedania="%s"]/./Direccion/text()'%pueblo)
            centro = doc.xpath('//Centro[//Localizacion[Pedania="%s"]]/text()'%pueblo)
            return zip(calle,centro)

        for calle,centros in poblacion(doc):
            print (centros," - ",calle)


    if opcion==4:










    if opcion==5:

    elif opcion == 0:
        break;
    else:
        print ("Esa opcion no existe")
