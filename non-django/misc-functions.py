import json
from datetime import datetime
import statsmodels.api as sm
from numpy import array

import seaborn as sns

def crop_factor(day):
    '''
    Returns the crop factor(Kc) of a given crop and how long it's in the ground.
    parameters:
    crop = str
    day = int
    return = float
    >> crop_factor("Brocolli", 99)
    >> 1.04
    '''
    with open("./data/cropdata.json", "r") as cropfile:
        data = json.load(cropfile)[crop]
    # determining stage
    if day < data["initial_length"]:
        return data["initial_kc"]
    elif day <  data["initial_length"] + data["interpolate_length"]:
        x = day - data["initial_length"]
        dy = (data["mid_kc"] - data["initial_kc"]) / data["interpolate_length"]
        total = data["initial_kc"] + x * dy
        return total
    elif day <  data["initial_length"] + data["interpolate_length"] + data["mid_length"]:
        return data["mid_kc"]
    else:
        return data["end_kc"]


def fallback_ET():
    today = datetime.now()
    # converts today to an tuple of year, month, etc.
    # then we take the 7th value of the tuple
    year_day = today.utctimetuple()[7] 
    with open("./data/PET_paramaribo.json", "r") as etfile:
        et = json.load(etfile)[year_day]
    return et


def measured_evaporation():
    '''
    this is the one that actually measures.
    call a function to measure the distance, and multiply with pan factor.
    Additionally, we need to set some logic to ignore if the value dropped below x ammount,
    because then it means that the autosiphon was recently used
    Make it return an ERROR when it detects autosiphon or float valve use
    '''
    return None


def evaporation_today(crop, day):
    '''
    this is the function which should be used to get the evapotranspiration of a given plant
    '''
    Kc = crop_factor(crop, day)
    # check model for panfactor
    # get measured_et. if ERROR, fall back to fallback_ET
    # multiply Kc with ET
    # return it
    return None





# IGNORE
# with open("./data/cropdata.json", "r") as cropfile:
#         data = json.load(cropfile)

# for k, v in data:
#     self = v
#     initial = [[], []]
#     for i in range(self.initial_length):
#         initial[0].append(i)
#         initial[1].append(self.initial_kc)

#     interpolate = [[], []]
#     for i in range(self.initial_length, self.initial_length + self.interpolate_length):
#         interpolate[0].append(i)
#         interpolate[1].append(self.crop_factor(i))

#     mid = [[], []]
#     start = self.initial_length + self.interpolate_length
#     for i in range(start, start + self.mid_length):
#         mid[0].append(i)
#         mid[1].append(self.mid_kc)

#     end=[[], []]
#     start += self.end_length
#     for i in range(start, start + self.end_length):
#         mid[0].append(i)
#         mid[1].append(self.end_kc)
#     sns.lineplot(x=initial[0], y=initial[1])
#     sns.lineplot(x=interpolate[0], y=interpolate[1])
#     sns.lineplot(x=mid[0], y=mid[1])
#     sns.lineplot(x=end[0], y=end[1])
#     plt.show()