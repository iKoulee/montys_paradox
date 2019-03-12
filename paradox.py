#!/usr/bin/env python

from __future__ import division
import random
import sys

def openFalse(doors, pick):
    for i in range(len(doors)):
        if pick == i:
            continue;
        if doors[i] == False:
            doors[i] = None;
            break;
## end openFalse

def gamersChance(doors, switch, pick):
    if (switch == False):
        #print("I wont change")
        return pick
    else:
        #print("I will change")
        pass
    for i in range(len(doors)):
        if (doors[i] != None):
            if (i == pick):
                continue;
            return i;
## end gamersChance

def game(changeOption, debug):
    doors = [False, False, False]
    doors[random.randint(0, 2)] = True;
    if (debug):
        print("Doors: ", doors)
    pick = random.randint(0, 2);
    if (debug):
        print("Pick:", pick)
    openFalse(doors, pick);
    if (debug):
        print("Reveal doors:", doors)
    pick = gamersChance(doors, changeOption, pick)
    if (debug):
        print("New pick:", pick)
    return doors[pick]

if len(sys.argv) > 1:
    changeOption = sys.argv[1] in ["true", "True", "TRUE"]
if len(sys.argv) > 2:
    gamesCount = int(sys.argv[2])
else:
    changeOption = False
    gamesCount = 1

print("Do we change a pick?", changeOption)
print("We will play " + str(gamesCount) + " times")

results = {True: 0, False: 0};
for gameNum in range(gamesCount):
    results[game(changeOption, False)] += 1

print("Wictory rate: " + str( (results[True]/gamesCount)*100 ) + "%")
print("Lose rate: " + str((results[False]/gamesCount)*100) + "%")

