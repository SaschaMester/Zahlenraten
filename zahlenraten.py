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

# Konfiguration
minZahl = 1
# Der Minimalwert für das Zahlenratespiel kann hier geändert werden

maxZahl = 100
# Die Maximalwert für das Zahlenratespiel kann hier geändert werden

versuche = 5
# Die Anzahl der Rateversuche kann hier konfiguriert werden.

ausgedachteZahl = randint(minZahl, maxZahl)
# Zahl ausdenken


print("Ich habe mir eine Zahl zwischen {}  und {} ausgedacht." . format(minZahl, maxZahl))
print("Sie haben {} Versuche, meine Zahl zu erraten." . format(versuche))

def raten(): 
  # Die Funktion raten() stellt die eigentliche Funktionalität des Programmes zur Verfügung
  for count in range(0, versuche):
    zahl = int(input("Bitte geben Sie nun Ihren {}. Rateversuch ein: " . format(count+1))) 
    # Da der Computer bei 0 zu zählen beginnt, wäre der 1. Rateversuch der "0. Versuch" - also addieren wir 1 
    if zahl < ausgedachteZahl:
      # Eingegebene Zahl mit der zu ratenden Zahl vergleichen
      print ("Meine Zahl ist größer als {}" . format(zahl))
      if count == versuche - 1: 
        # Aus dem gleichen Grund, warum oben 1 addiert wurde, subtrahieren wir hier wieder um 1
        print("Sie haben es in {} Versuchen nicht geschafft, die Zahl {} zu erraten und haben verloren" . format(versuche, ausgedachteZahl))
        # Game Over und Lösung verraten
    elif zahl > ausgedachteZahl:
      print("Meine Zahl ist kleiner als {}" . format(zahl))
      if count == versuche - 1: 
        print("Sie haben es in {} Versuchen nicht geschafft, die Zahl {} zu erraten und haben verloren" . format(versuche, ausgedachteZahl))
    else:
      # Spiel gewonnen
      print("RICHTIG!")
      print("Sie haben {} Versuche benötigt." . format(count+1))
      exit()

raten()
