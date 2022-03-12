# Importing
import random
import time
import os
import sys
import colorama as cr
cr.init(autoreset = True)

# Wall: █
# Ground: ⠀
# Ground Texture: ▒
# Player: 🐁
# Kaas: 🧀
# Taco: 🌮
# Sleutel 1: 🔑
# Sleutel 2: 🗝️
# Deur: 🚪

class player:
    def __init__(self):
        self.name = 'playername'
        self.level = 'level1'

player = player()
name = player.name

title = ""
levelLine0 = "levelLine0"
levelLine1 = "levelLine1"
levelLine2 = "levelLine2"
levelLine3 = "levelLine3"
levelLine4 = "levelLine4"
levelLine5 = "levelLine5"
levelLine6 = "levelLine6"
levelLine7 = "levelLine7"
map = "map"

completed = ""

levelLineWall = "█████████████████████████████████████████████████"

levels = {
	"level1": {
		title: "",
		completed: 0,
		map: {
			levelLine0: "██⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██",
			levelLine1: "██⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██",
			levelLine2: "██⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██⠀⠀⠀⠀⠀⠀⠀⠀██████████████████⠀⠀⠀⠀⠀⠀⠀██",
			levelLine3: "██⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██⠀⠀⠀⠀⠀⠀⠀⠀██⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██",
			levelLine4: "██⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██⠀⠀⠀⠀⠀⠀⠀⠀██⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██",
			levelLine5: "██⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██⠀⠀⠀⠀⠀⠀███████████████████",
			levelLine6: "██⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██",
			levelLine7: "██⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🌮⠀⠀⠀██"
		}	
	}
}

currentLevel = ("level1")

def levelLogic():
	if player.level == "level1":
		llList = list(levels[currentLevel][map][levelLine2])
		llList[6] = "🐁"
		llList[7] = ""
		levels[currentLevel][map][levelLine2] = "".join(llList)
	if player.level == "level2":
		pass

def createLevel():

	
	
	print(levelLineWall)
	for x in levels[currentLevel][map]:
		print(levels[currentLevel][map][x])
	print(levelLineWall)

def movement():
	pass


levelLogic()
createLevel()