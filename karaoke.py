#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from urllib.request import urlretrieve
import sys
import smallsmilhandler
import json

class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fichero):
        parser = make_parser()
        smilhandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(smilhandler)
        parser.parse(open(fichero))
        self.etiquetas = smilhandler.get_tags()

    def __str__(self):
        for etiqueta in self.etiquetas:
            lista = []
            lista.append(etiqueta['name'])
            for atributo in etiqueta:
                if atributo != 'name' and etiqueta[atributo] != "":
                    lista.append('\t' + atributo + '="' + etiqueta[atributo] +'"')
        return(lista)

    def to_json(self):
        json.dump(selfetiquetas, open('karaoke.json', 'w'))

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python3 karaoke.py file.smil")

    karaoke = KaraokeLocal(sys.argv[1])

    for etiqueta in smilhandler.etiquetas:
        lista = []
        lista.append(etiqueta['name'])
        for atributo in etiqueta:
            if atributo != 'name' and etiqueta[atributo] != "":
                lista.append('\t' + atributo + '="' + etiqueta[atributo] +'"')
                if atributo == 'src' and not etiqueta[atributo].find('http'):
                    nombre = etiqueta[atributo]
                    urlretrieve(nombre, nombre.split('/')[-1])
        print(' '.join(lista))
    json.dump(smilhandler.etiquetas, open('karaoke.json', 'w'))
