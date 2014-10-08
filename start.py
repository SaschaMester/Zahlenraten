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

from zahlenraten import *

# Die Funktion "start" des Zahlenrate-Moduls erwartet 3 Argumente: 
# Die kleinstmögliche Zahl, die größtmögliche Zahl und die Anzahl der
# Versuche. 
# Um beispielsweise den Computer eine Zahl zwischen 1 und 100 ausdenken 
# zu lassen, die der Benutzer in 5 Versuchen zu erraten hat, 
# ist die Funktion start() mit den Argumenten 1, 100, 5 aufzurufen. 
# start(1, 100, 5) bedeutet also:
# Der Computer denkt sich eine Zahl zwischen 1 und 100 aus, 
# der Spieler hat 5 Versuche, die Zahl zu erraten. 
# Dies sind jedoch lediglich die Einstellungen für den START des Spieles. 
# Errät der User die vom Computer ausgedachte Zahl, darf er in eine nächste
# Runde - in welcher sich diese Werte verändern können.

start(1, 100, 5)
