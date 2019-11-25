import json

class load_json:
    def __init__(self,database):
        js_data = open(database).read()
        self.Data = json.loads(js_data)

    def get_json(self):
        return self.Data