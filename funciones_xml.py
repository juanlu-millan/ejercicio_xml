#Lista conctatos de cada colegio que no pertenece a la pedania de lorca
def contacto(doc):
    lista = doc.xpath('''//Localizacion[not(Pedania='Lorca')]/../Centro/text() |
    //Localizacion[not(Pedania='Lorca')]/../Contacto/Web/text() |
    //Localizacion[not(Pedania='Lorca')]/../Contacto/Telefono/text() |
    //Localizacion[not(Pedania='Lorca')]/../Contacto/Email/text()
    //Localizacion[not(Pedania='Lorca')]/../Contacto/Fax/text()
    ''')
    return lista
#Cuenta los colegios que no tiene página web y muestra su nombre
def colegio(doc):
    lista = doc.xpath("//Contacto[not(Web)]/../Centro/text()")
    return lista


#Pide una pedania y muestra el nombre de los colegios y su dirección
def poblacion(pueblo,doc):
    calle = doc.xpath('//Localizacion[Pedania="%s"]/./Direccion/text()'%pueblo)
    centro = doc.xpath('//Centro[//Localizacion[Pedania="%s"]]/text()'%pueblo)
    return zip(calle,centro)

#Introduce un número de teléfono y muestra el Centro al que pertenece
def telefono(telefono,doc):
    centro =  doc.xpath('//Contacto[Telefono="%s"]/../Centro/text()'%telefono)
    return centro

#Introduce nombre del Instituto y te da un enlace a OpenStreetMap de su localización

def localizar(centro,doc):
    latitud = doc.xpath('//colegio_lorca[Centro="%s"]/Localizacion/Coordenadas/Latitud/text()'%centro)
    longitud = doc.xpath('//colegio_lorca[Centro="%s"]/Localizacion/Coordenadas/Longitud/text()'%centro)

    localizador="http://www.openstreetmap.org/#map=16/%s/%s"%(latitud[0],longitud[0])

    return localizador
