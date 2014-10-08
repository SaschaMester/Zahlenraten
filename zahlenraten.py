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
  if ausgedachteZahl > 65536:
    maxZahl = 65536
    start(minZahl, maxZahl, versuche)
  if ausgedachteZahl > 500 and ausgedachteZahl < 1000 and versuche < 20:
    versuche = versuche * 2
  elif ausgedachteZahl > 2500 and versuche < 30:
    versuche = versuche * 3
  if versuche > 15000:
    versuche = 15000
  print("Ich habe mir eine Zahl zwischen {} und {} ausgedacht. Sie haben {} Versuche, meine Zahl zu erraten." . format(minZahl, maxZahl, versuche))
  print("Sie haben {} Versuche, meine Zahl zu erraten." . format(versuche))
  print("Durch Eingabe von 0 beenden Sie das Programm")
  __raten(ausgedachteZahl, minZahl, maxZahl, versuche)

def __raten(ausgedachteZahl, minZahl, maxZahl, versuche): 
  # Die Funktion raten() stellt die eigentliche Funktionalität des Programmes zur Verfügung
  for count in range(0, versuche):
    zahl = int(input("Bitte geben Sie nun Ihren {}. Rateversuch ein: " . format(count+1))) 
    if zahl == 0:
      __ende()
    if zahl != ausgedachteZahl and count != versuche - 1:
      print("Falsch!")
      if versuche - count - 1 != 1:
        print("Sie haben noch {} Versuche." . format(versuche - count - 1))
      else:
        print("Sie haben noch 1 Versuch.")
    if zahl != ausgedachteZahl and count == versuche - 1:
      print("Sie haben es in {} Versuchen nicht geschafft, die Zahl {} zu erraten." . format(versuche, ausgedachteZahl))
      __ende()
    if zahl < ausgedachteZahl:
      # Eingegebene Zahl mit der zu ratenden Zahl vergleichen
      print ("Meine Zahl ist größer als {}" . format(zahl))
    elif zahl > ausgedachteZahl:
      print("Meine Zahl ist kleiner als {}" . format(zahl))
    else:
      # Spiel gewonnen
      print("RICHTIG!")
      print("Sie haben {} Versuche benötigt." . format(count+1))
      start(minZahl, maxZahl * 2 - count - 1, versuche * 2 - count - 1)

def __ende():
  print ("Das Programm wird beendet!")
  print ("Auf Wiedersehen!")
  exit()

