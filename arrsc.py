#!/usr/bin/env python
import argparse, os, time

parser = argparse.ArgumentParser(description="Exemple de programme avec arguments")
parser.add_argument("filename", help="Nom du fichier (obligatoire)")
parser.add_argument("-o", "--destination", help="Nom du deuxième fichier (optionnel)")

# Parser les arguments du terminal
args = parser.parse_args()

# Récupérer la valeur de l'argument obligatoire "filename"
filename = os.getcwd()+os.path.sep+args.filename

# Récupérer la valeur de l'argument optionnel "filename2"
destination = (os.getcwd()+os.path.sep+args.destination) if not args.destination is None else None

# Afficher les valeurs des arguments
# print("Nom du fichier 1: ", filename)
# print("Nom du fichier 2: ", destination)
# time.sleep(10000)


from main_compiler import compile
compile(filename, destination)
