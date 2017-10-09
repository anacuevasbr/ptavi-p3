#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        """
        Constructor. Inicializamos las variables
        """
        self.etiquetas = []
        self.lista_etiq = ["root-layout", "region", "img", "audio", "textstream"]
        self.coleccion_attr = {'root-layout': ['width', 'height', 'background-color'],
                            'region': ['id', 'top', 'bottom', 'left', 'right'],
                            'img': ['src', 'region', 'begin', 'dur'],
                            'audio': ['src', 'begin', 'dur'],
                            'textstream':['src', 'region']}


    def startElement(self, name, attrs):

        if name in self.lista_etiq:
            Dict = {}
            Dict['name'] = name
            for atributo in self.coleccion_attr[name]:
                Dict[atributo] = attrs.get(atributo, "")
            self.etiquetas.append(Dict)

    def get_tags(self):
        return self.etiquetas

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    smilhandler = SmallSMILHandler()
    parser.setContentHandler(smilhandler)
    parser.parse(open('karaoke.smil'))
    print(smilhandler.get_tags())
