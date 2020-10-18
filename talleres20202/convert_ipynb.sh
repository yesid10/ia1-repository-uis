#!/bin/bash
echo "uno: $1 dos $2"
cp $2.ipynb ../$1.ipynb
if [ ! -f ../$1".ipynb" ]; then
echo "ERROR!: NO FUE POSIBLE CREAR EL ARCHIVO!."
else
echo "¡PERFECTO!, el archivo   '$1.ipynb'   se creó correctamente :D"
fi
