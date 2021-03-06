#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from urllib.request import urlretrieve
import sys
import smallsmilhandler
import json


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):
    """ clase para gestinar karaoke de tipo smil
    """

    def __init__(self, fichero):
        """inicializador, llama al parser y crea estructura de datos
        """
        parser = make_parser()
        smilhandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(smilhandler)
        parser.parse(open(fichero))
        self.etiquetas = smilhandler.get_tags()

    def __str__(self):
        """Devuelve un string con todos los datos
        """
        lista = []
        for etiqueta in self.etiquetas:
            lista.append(etiqueta['name'])
            for atributo in etiqueta:
                if atributo != 'name' and etiqueta[atributo] != "":
                    lista.append('\t' + atributo + '="' + etiqueta[atributo] +
                                 '"')
            lista.append('\n')
        return(''.join(lista))

    def to_json(self, fichero, fichj=''):
        """Convierte nuestra estructura de datos en un json
        """
        if fichj == '':
            fichj = fichero.split('.')[0] + '.json'
        json.dump(self.etiquetas, open(fichj, 'w'))

    def do_local(self):
        """descarga archivos y modifica para que esten en local
        """
        for etiqueta in self.etiquetas:
            for atributo in etiqueta:
                if atributo == 'src' and not etiqueta[atributo].find('http'):
                    nombre = etiqueta[atributo]
                    urlretrieve(nombre, nombre.split('/')[-1])
                    etiqueta[atributo] = nombre.split('/')[-1]

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python3 karaoke.py file.smil")
    try:
        karaoke = KaraokeLocal(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File doesn't exist")

    print(karaoke)
    karaoke.to_json(sys.argv[1])
    karaoke.do_local()
    karaoke.to_json(sys.argv[1], 'local.json')
    print(karaoke)
