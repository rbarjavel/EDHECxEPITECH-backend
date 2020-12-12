import IA.gui_deepchat as ia
import os
import json

class IA():

    def __init__(self):
        self.weltek = ia.weltekIA()
        self.result = dict()
        self.arr = ["type", "color", "tissue", "size"]

    def runProcesse(self, msg):
        self.result.clear()

        print(msg)
        for strr in self.arr:
            pred = self.weltek.predict_class(msg, strr)
            res = self.weltek.get_response(pred)

            self.result[strr] = res

        return self.result