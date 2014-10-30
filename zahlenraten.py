#! /usr/bin/env python3
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



def start(minZahl, maxZahl):
  # Invert negative values
  minZahl = abs(minZahl)
  maxZahl = abs(maxZahl)

  if abs(maxZahl - minZahl) < 5:
    print("Um effektiv spielen zu können, sollte der Unterschied zwischen Mindestwert und Maximalwert")
    print("durchaus größer sein als 5.")
    quit()

  # Make sure that "minZahl" is less than "maxZahl"
  if maxZahl < minZahl:
    minZahl1 = maxZahl
    maxZahl1 = minZahl
    maxZahl = maxZahl1
    minZahl = minZahl1

  #Choose a random number out of the given pool
  ausgedachteZahl = randint(minZahl, maxZahl)
  print("Ich habe mir eine Zahl zwischen {} und {} ausgedacht." . format(minZahl, maxZahl))
  print("Ihre Aufgabe ist es, meine Zahl zu erraten.")
  print("Mit einer Zahl, die kleiner ist als {}, beenden Sie das Programm." . format(minZahl))
  main(minZahl, maxZahl, ausgedachteZahl)


def main(minZahl, maxZahl, ausgedachteZahl):
  # main Procedure
  geraten = False
  while not geraten:
    userzahl = input("Bitte geben Sie Ihren Rateversuch ein: ")
    
    try:
      userzahl = int(userzahl)
      userzahl = abs(userzahl)
    except ValueError:
      print("Bitte nur Ganzzahlen eingeben!")
      continue
    if userzahl > maxZahl:
      print("Meine Zahl ist nicht größer als {}." . format(maxZahl))
      continue
    if userzahl < minZahl:
      print("Auf Wiedersehen!")
      quit()

    if userzahl > ausgedachteZahl:
      print("Meine Zahl ist kleiner als {}". format(userzahl))
    elif userzahl < ausgedachteZahl:
      print("Meine Zahl ist größer als {}" . format(userzahl))
    else:
      geraten = True
      print("Herzlichen Glückwunsch!")
      play_again = input("Nochmal spielen? (Mit den gleichen Einstellungen) (J/N) ")
      if play_again == "j" or play_again == "J":
        start(minZahl, maxZahl)
