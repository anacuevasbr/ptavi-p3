#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler
import json

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python3 karaoke.py file.smil")

    parser = make_parser()
    smilhandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(smilhandler)
    parser.parse(open(sys.argv[1]))

    for etiqueta in smilhandler.etiquetas:
        lista = []
        lista.append(etiqueta['name'])
        for atributo in etiqueta:
            if atributo != 'name':
                lista.append('\t' + atributo + '="' + etiqueta[atributo] +'"')
        print(' '.join(lista))
    json.dump(smilhandler.etiquetas, open('karaoke.json', 'w'))
