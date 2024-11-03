#!/bin/bash


cd "/home/camilo/Documentos/python-eco/control-peso"

ruta=$(pwd)

if [ $ruta == "/home/camilo/Documentos/python-eco/control-peso" ]; then
    source env/bin/activate
fi


python "/home/camilo/Documentos/python-eco/control-peso/main.py"

