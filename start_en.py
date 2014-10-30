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

from guessthenumber import *

numbersEntered = False

print("Welcome to this tiny game") 
print("======================================")
print("Please choose a range for the computer to choose a number.")
while not numbersEntered:
  try:
    minNumber = int(input("Please type in the minimum number: "))
    maxNumber = int(input("Please type in the maximum number: "))
  except ValueError:
    print("Only integers allowed")
    continue
  numbersEntered = True

start(minNumber, maxNumber)
