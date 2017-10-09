#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python3 karaoke.py file.smil")

    parser = make_parser()
    smilhandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(smilhandler)
    parser.parse(open(sys.argv[1]))

    for etiqueta in smilhandler.etiquetas:
        lista = []
        lista.append(etiqueta['nombre'])
        for atributo in etiqueta:
            if atributo != 'nombre':
                lista.append(atributo)
                lista.append(etiqueta[atributo])
        print(lista.join())
