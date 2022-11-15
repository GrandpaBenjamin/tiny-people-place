import os
import json
import datetime
import openai

class World:
    def __init__(self, saveLocation, worldSettings):
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

    def tick(self):
        pass

    def getNewWorldName(self):
        return openai.Completion.create(
            model="text-davinci-002",
            prompt="a world name in a fantasy universe.",
            max_tokens=6,
            temperature=0
        )["choices"][0]["text"].replace("\n","")
    

    def createSaveData(self):
        newWorldData = {
            "universe": {
                "name": "New Universe",
                "creation-date": datetime.datetime.now(),
                "planets": [
                    {
                        "name": self.getNewWorldName(),
                        "creation-date": datetime.datetime.now(),
                    },
                ],
            }
        }
        return newWorldData
        