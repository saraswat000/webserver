import json

class loadTeam:
    def __init__(self, database):
        jsdata = open(database).read()
        self.JsonData = json.loads(jsdata)

    def getTeam(self):
        return self.JsonData