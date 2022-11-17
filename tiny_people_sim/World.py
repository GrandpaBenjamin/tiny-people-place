import os
import json
import datetime
import openai
import random
from tiny_people_sim.Entities import Animal
import helper

class World:
    def __init__(self, saveLocation, worldSettings):
        self.saveLocation = saveLocation
        self.worldSettings = worldSettings

        # initialize openAI key
        openai.api_key = os.getenv("OPENAI_API_KEY")

        # check if save exists. 
        if os.path.exists(saveLocation) and os.path.getsize(saveLocation) > 0 and json.loads(open(saveLocation).read()) != {}:
            print("file exists and is not empty")
        else: # if not create new save
            print("file either doesnt exist or is empty")
            saveFile = open(saveLocation,'w')
            saveFile.write(json.dumps(self.createSaveData()))
            saveFile.close()

        self.SAVEDATA = json.loads(open(saveLocation).read()) # read save data from provided save file

    def save(self):
        saveFile = open(self.saveLocation,"w")
        saveFile.write(json.dumps(self.SAVEDATA))
        saveFile.close()


    def tick(self):
        #enter tick code here

        #saving
        self.save()

    def getNewWorldName(self):
        return openai.Completion.create(
            model="text-davinci-002",
            prompt="a world name in a fantasy universe.",
            max_tokens=6,
            temperature=0
        )["choices"][0]["text"].replace("\n","")
    
    def getGalaxyName(self):
        baseName = helper.numberToLetter(random.randint(1,26))
        baseName += helper.numberToLetter(random.randint(1,26))
        return baseName+str(random.randint(1,99))

    def generateInitialGalaxies(self,count,planetCount):
        data = []
        galaxyNames = []
        data.append([])
        for i in range(count):
            while True:
                name = "galaxy " + self.getGalaxyName()
                if not name in galaxyNames:
                    break
            galaxyNames.append(name)
            data.append({
                "name": name,
                "creation-data": str(datetime.datetime.now()),
                "data": self.generateInitialPlanets(planetCount)
            })
        data[0] = galaxyNames
        return data

    def generateInitialPlanets(self,count):
        data = []
        planetNames = []
        data.append([])
        for i in range(count):
            while True:
                name = "planet " + self.getGalaxyName()
                if not name in planetNames:
                    break
            planetNames.append(name)
            data.append({
                "name": name,
                "creation-date": str(datetime.datetime.now()),
                "data": self.generatePlanetData()
            })
        data[0] = planetNames
        return data
    
    def generateGalaxy(self,galaxyNames,planetNames):
        data = []
        data.append([])
        while True:
            name = "galaxy " + self.getGalaxyName()
            if not name in galaxyNames:
                break
        galaxyNames.append(name)
        data.append({
            "name": name,
            "creation-data": str(datetime.datetime.now()),
            "data": self.generatePlanet(planetNames)
        })
        return data

    def generatePlanet(self,planetNames):
        data = []
        planetNames = []
        count = 1
        for i in range(count):
            while True:
                name = "planet " + self.getGalaxyName()
                if not name in planetNames:
                    break
            planetNames.append(name)
            data.append({
                "name": name,
                "creation-data": str(datetime.datetime.now()),
                "data": self.generatePlanetData()
            })
        return data

    def generatePlanetData(self):
        landCoverage = random.randint(0,100)
        data = {
            "land": {
                "coverage": landCoverage
            },
            "water": {
                "coverage" : 100-landCoverage
            }
        }
        return data

    def createSaveData(self):
        newWorldData = {
            "universe": {
                "name": "Tiny People Universe",
                "creation-date": str(datetime.datetime.now()),
                "Galaxies": self.generateInitialGalaxies(2,4), # number of initial galaxies, number of initial planets
            }
        }
        return newWorldData
        