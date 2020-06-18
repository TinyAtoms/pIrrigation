import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import json

with open("./data/cropdata.json", "r") as crop:
    data = json.load(crop)


for k, v in data.items():
    name = k
    init_l = v["initial_length"]
    init_k = v["initial_kc"]
    inter_l = v["interpolate_length"] + init_l
    mid_l = v["mid_length"] + inter_l
    mid_k = v["mid_kc"]
    end_l = v["end_length"] + mid_l
    end_k = v["end_kc"]
    df = pd.DataFrame({"day": [], "kc" : [], "stage": [] })
    dy = (mid_k - init_k) / v["interpolate_length"]
    for i in range(1, end_l):
        if i < init_l:
            row = {"day": i, "kc" : init_k, "stage": "initial" }
            df = df.append(row, ignore_index=True)
        elif i < inter_l:
            row = {"day": i, "kc" : init_k + (i - init_l) * dy, "stage": "Growth" }
            df = df.append(row, ignore_index=True)
        elif i < mid_l:
            row = {"day": i, "kc" : mid_k, "stage": "mid" }
            df = df.append(row, ignore_index=True)
        else:
            row = {"day": i, "kc" : end_k, "stage": "End" }
            df = df.append(row, ignore_index=True)

    df = df.append({"day": init_l, "kc" : init_k, "stage": "initial" }, ignore_index=True)
    df = df.append({"day": inter_l, "kc" : mid_k, "stage": "Growth" }, ignore_index=True)
    sns.lineplot(x="day", y="kc", hue="stage", data=df)
    plt.ylim([0,2])
    plt.title(name)
    plt.show()
    break
    # need to generate all charts and save them
