#!/bin/bash

FILE="efface_moi"

if test -f "$FILE"; then
	rm "$FILE"
	echo "Fichier correctement efface"
else
	echo "Ce fichier n'existe pas"
fi

