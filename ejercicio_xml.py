from lxml import etree
doc = etree.parse('colegios-lorca.xml')

#Lista conctatos de cada colegio que no pertenece a la pedania de lorca
def colegio(doc):
    lista = doc.xpath("//Web/text() | //Email/text() | //Telefono/text() | //Fax/text()")
    return lista
