import gui_deepchat as ia

weltek = ia.weltekIA()

weltek.retrain_model("type")
weltek.retrain_model("color")
weltek.retrain_model("tissue")
weltek.retrain_model("size")