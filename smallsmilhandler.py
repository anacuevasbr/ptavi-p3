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
            region = {}
            self.etiquetas.append(region)
        elif name == "img":
            img = {}
            self.etiquetas.append(img)
        elif name == "audio":
            audio = {}            
            self.etiquetas.append(audio)
        elif name == "textstream":
            textstream = {}
            self.etiquetas.append(textstream)

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    smilhandler = SmallSMILHandler()
    parser.setContentHandler(smilhandler)
    parser.parse(open('karaoke.smil'))
    print(smilhandler.etiquetas)
    print(smilhandler.etiquetas[0])
    print(smilhandler.etiquetas[0]['etiqueta'])
