import gui_deepchat as ia
import os
import json

weltek = ia.weltekIA()

msg = "je cherche une robe avec une couleur noire fait de coton en taille xs"

result = dict()

ints = weltek.predict_class(msg, "type")
res = weltek.get_response(ints)
result['type'] = res

ints = weltek.predict_class(msg, "color")
res = weltek.get_response(ints)
result['color'] = res

ints = weltek.predict_class(msg, "tissue")
res = weltek.get_response(ints)
result['tissue'] = res

ints = weltek.predict_class(msg, "size")
res = weltek.get_response(ints)
result['size'] = res

print(result)