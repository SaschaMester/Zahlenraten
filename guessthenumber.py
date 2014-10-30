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


# Import random method
from random import randint



def start(minNumber, maxNumber):
  # Invert negative values
  minNumber = abs(minNumber)
  maxNumber = abs(maxNumber)

  # Make sure that "minZahl" is less than "maxZahl"
  if maxNumber < minNumber:
    minNumber1 = maxNumber
    maxNumber1 = minNumber
    maxNumber = maxNumber1
    minNumber = minNumber1

  #Choose a random number out of the given pool
  numberToGuess = randint(minNumber, maxNumber)
  print("I chose a number between {} and {}." . format(minNumber, maxNumber))
  print("Can you guess my number?")
  print("You can type a number less than {} to quit." . format(minNumber))
  main(minNumber, maxNumber,numberToGuess)


def main(minNumber, maxNumber, numberToGuess):
  # main Procedure
  guessed = False
  while not guessed:
    userNumber = input("Please type in your guess: ")
    
    try:
      userNumber = int(userNumber)

      # Avoid negative Values
      userNumber = abs(userNumber)

    except ValueError:
      print("Only integer allowed!")
      continue
    if userNumber < minNumber:
      print("Goodbye!")
      quit()

    if userNumber > numberToGuess:
      print("My number is less than {}". format(userNumber))
    elif userNumber < numberToGuess:
      print("My number is bigger than {}" . format(userNumber))
    else:
      guessed = True
      print("Congratulations!")
      play_again = input("Play again? (With the same settings) (Y/N) ")
      if play_again == "y" or play_again == "Y":
        start(minNumber, maxNumber)
