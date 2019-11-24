import json

class load_features:
    def __init__(self,database):
        js_data = open(database).read()
        self.features = json.loads(js_data)

    def get_features(self):
        return self.features