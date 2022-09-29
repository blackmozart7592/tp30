# /bin/bash

from random import*
fichier = open("dico.txt", "r")
liste_mots = fichier.readlines()    # met tous les mots du fichiers dans une liste
mot = choice(liste_mots)            # prend au hasard un mot dans la liste
mot = mot.rstrip()                  # supprime le caractère "saut à la ligne"
fichier.close()

mot_devine = "-" * len(mot)
print(mot_devine)

while mot_devine!=mot:
  lettre=input("Entrez une lettre : ")
  for i in range(len(mot)):
    if lettre==mot[i]:
      mot_devine = mot_devine[:i] + lettre + mot_devine[i+1:]
  print(mot_devine)
if mot == mot_devine:
  print 'Bravo ! Le mot',mot,'a été trouvé'
          
