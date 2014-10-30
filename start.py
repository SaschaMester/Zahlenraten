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

from zahlenraten import *

zahlenEingegeben = False

print("Herzlich Willkommen im Zahlenratespiel") 
print("======================================")
print("Sie dürfen nun den Zahlenbereich eingeben, innerhalb welchem der Computer")
print("Sich eine Zahl ausdenken soll.")
while not zahlenEingegeben:
  try:
    minZahl = int(input("Bitte geben Sie die Mindestzahl ein: "))
    if minZahl == 0:
      print("Negative Werteingaben werden im Hauptprogramm per Multiplikation mit -1")
      print("in positive Werte umgewandelt.") 
      print("Da Sie in der Raterunde mit jedem Rateversuch, der kleiner ist, als der Mindestwert,")
      print("das Programm beenden können, und Sie nicht daran gehindert werden sollen, das Programm")
      print("sauber zu beenden, ist die 0 als Mindestzahl nicht zulässig.")
      print("Das Programm wird an dieser Stelle beendet.")
      quit()

    maxZahl = int(input("Bitte geben Sie die Maximalzahl ein: "))
  except ValueError:
    print("Es sind nur Ganzzahlen erlaubt:")
    continue
  zahlenEingegeben = True

start(minZahl, maxZahl)

