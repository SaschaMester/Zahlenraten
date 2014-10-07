#! /usr/bin/env python
# -*- coding: utf-8

########################################
############# Zahlenraten ##############
########################################
# (c) 2014 by Sascha Mester            #
# This program is free software.       #
# You can freely redistribute it       #
# under the terms of the               #
# GNU General Public License,          #
# version 3 or ( at your opinion )     #
# any later version, published by      #
# the Free Software Foundation.        #
########################################
# This program is published in the     #
# hope that it will be useful,         #
# but WITHOUT ANY WARRANTY, without    #
# even the implied warranty of         #
# MERCHANDIBILITY of FITNESS FOR A     #
# PARTICULAR PURPOSE. See the          #
# GNU GENERAL PUBLIC LICENSE for       #
# more details.                        #
########################################


# Zufallsfunktion importieren
from random import randint


def start(minZahl, maxZahl, versuche):
  ausgedachteZahl = randint(minZahl, maxZahl)
  print("Ich habe mir eine Zahl zwischen {} und {} ausgedacht." . format(minZahl, maxZahl))
  print("Sie haben {} Versuche, meine Zahl zu erraten." . format(versuche))
  print("Durch Eingabe von 0 beenden Sie das Programm")
  raten(ausgedachteZahl, versuche)

def raten(ausgedachteZahl, versuche): 
  # Die Funktion raten() stellt die eigentliche Funktionalität des Programmes zur Verfügung
  for count in range(0, versuche):
    zahl = int(input("Bitte geben Sie nun Ihren {}. Rateversuch ein: " . format(count+1))) 
    if zahl == 0:
      exit()
    if zahl != ausgedachteZahl and count != versuche - 1:
      if versuche - count - 1 != 1:
        print("Sie haben noch {} Versuche." . format(versuche - count - 1))
      else:
        print("Sie haben noch 1 Versuch.")
    if zahl != ausgedachteZahl and count == versuche - 1:
      print("Sie haben es in {} Versuchen nicht geschafft, die Zahl {} zu erraten." . format(versuche, ausgedachteZahl))
      exit()
    if zahl < ausgedachteZahl:
      # Eingegebene Zahl mit der zu ratenden Zahl vergleichen
      print ("Meine Zahl ist größer als {}" . format(zahl))
    elif zahl > ausgedachteZahl:
      print("Meine Zahl ist kleiner als {}" . format(zahl))
    else:
      # Spiel gewonnen
      print("RICHTIG!")
      print("Sie haben {} Versuche benötigt." . format(count+1))
      exit()
