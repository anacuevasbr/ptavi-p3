#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        self.etiquetas = []

    def startElement(self, name, attrs):

        if name == "root-layout":
            root_layout = {'etiqueta': 'root-layout'}
            root_layout['width'] = attrs.get('width', "")
            root_layout['height'] = attrs.get('height', "")
            root_layout['background-color'] = attrs.get('background-color', "")
            self.etiquetas.append(root_layout)
        elif name == "region":
            region = {'etiqueta' : 'region'}
            region['id'] = attrs.get('id', "")
            region['top'] = attrs.get('top', "")
            region['bottom'] = attrs.get('bottom', "")
            region['left'] = attrs.get('left', "")
            region['right'] = attrs.get('right', "")
            self.etiquetas.append(region)
        elif name == "img":
            img = {'etiqueta' : 'img'}
            img['src'] = attrs.get('src', "")
            img['region'] = attrs.get('region', "")
            img['begin'] = attrs.get('begin', "")
            img['dur'] = attrs.get('dur', "")
            self.etiquetas.append(img)
        elif name == "audio":
            audio = {'etiqueta' : 'audio'}
            audio['src'] = attrs.get('src', "")
            audio['begin'] = attrs.get('begin', "")
            audio['dur'] = attrs.get('dur', "")
            self.etiquetas.append(audio)
        elif name == "textstream":
            textstream = {'etiqueta' : 'textstream'}
            textstream['src'] = attrs.get('src', "")
            textstream['region'] = attrs.get('region', "")
            self.etiquetas.append(textstream)

    def get_tags(self):
        print(self.etiquetas)

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    smilhandler = SmallSMILHandler()
    parser.setContentHandler(smilhandler)
    parser.parse(open('karaoke.smil'))
    smilhandler.get_tags()
    for etiqueta in smilhandler.etiquetas:
        print(etiqueta['etiqueta'])
