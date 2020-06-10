import seaborn
import json



def kc_graph(crop):
    with open("cropdata.json", "r") as jfile:
        cropdata = json.load(jfile)[crop]
    print(cropdata)

kc_graph("Tomato")
