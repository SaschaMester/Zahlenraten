#! /usr/bin/env python3
# ~*~ encoding: utf-8 ~*~

from random import randint

eingegeben = False
geraten = False

while not eingegeben:
  zahl = input("Bitte gebe eine Zahl > 50 ein: ")
  try:
    zahlInt = int(zahl)
  except ValueError:
    print("Nur Ganzzahlen erlaubt!")
    continue
  if zahlInt <= 50:
    continue

  eingegeben = True

try:
  ausgedachteZahl = randint(1, zahlInt)
except ValueError:
  print("Ungültige Eingabe")
  quit()


print("Ich habe mir eine Zahl zwischen 1 und " + zahl + " ausgedacht.")
print("Es ist an dir, meine Zahl zu erraten.")
while not geraten:
  userzahl = input("Bitte gebe deinen Rateversuch ein: ")
  try:
    userzahlInt = abs(int(userzahl))
  except ValueError:
    print("Es sind nur ganze Zahlen erlaubt!")
    continue
  if userzahlInt == 0:
    print("Auf Wiedersehen!")
    quit()
  if abs(userzahlInt) < ausgedachteZahl:
    print("Meine Zahl ist größer als " + userzahl + ".")
  elif abs(userzahlInt) > ausgedachteZahl:
    print("Meine Zahl ist kleiner als " + userzahl + ".")
  else:
    geraten = True

while geraten:
  print("Herzlichen Glückwunsch!")
  quit()

