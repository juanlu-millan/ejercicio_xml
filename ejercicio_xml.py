from lxml import etree
doc = etree.parse('colegios-lorca.xml')

# #Lista conctatos de cada colegio que no pertenece a la pedania de lorca
# def colegio(doc):
#
#     if doc.xpath(//Localizacion[not(Pedania='Lorca')]/text()):
#         lista = doc.xpath("//Web/text() | //Email/text() | //Telefono/text() | //Fax/text() | //Localizacion[not(Pedania='Lorca')]")
#
#     return lista
#
# for col in colegio(doc):
#     print(col)
#
# #Cuenta los colegios que no tiene página web y muestra su nombre
#
# def colegio(doc):
#     lista = doc.xpath("//Contacto[not(Web)]/../Centro/text()")
#     return lista
#
# for col in colegio(doc):
#     print(col)
#
# #Pide una pedania y muestra el nombre de los colegios y su dirección


def poblacion(doc):
    pueblo=input("Dime una pedania:").capitalize()
    calle = doc.xpath('//Localizacion[Pedania="%s"]/./Direccion/text()'%pueblo)
    centro = doc.xpath('//Centro[//Localizacion[Pedania="%s"]]/text()'%pueblo)
    return zip(calle,centro)

for calle,centros in poblacion(doc):
    print (centros," - ",calle)
