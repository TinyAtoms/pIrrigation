from datetime import datetime # to get date and hour
import asyncio # to make code asyncronous
import random # mocking rainfall 
import json # loading properties and such


# in mm
def rain_last_hour():
    # check rainfall
    # flush basin
    # FIXME :  we don't have anything to actually test this, so for now i'll add something dumb, like this
    rainfall = [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,2,2,2,3,3,3,1,1,1,1,1,1,1,0,0,0,0]
    return rainfall[random.randint(0, len(rainfall)-1)]


# asyncronous watering code. Means that multiple relays are opened up at the same time. 
# For more info how this works, https://docs.python.org/3/library/asyncio.html
# pretty sure we would connect the groups to 1 water connection, so it actually doesn't make sense to open multiple relays at the same time
# but i got this realisation today, and i wrote this code yesterday.
async def water(group, t):
    print("watering group {} now".format(group))
    # send actual signal to relay to start
    await asyncio.sleep(t)
    # send actual signal to relay to stop
    print("finished watering group", group)


async def water_groups(waterschedule):
    tasks = []
    for k, v in waterschedule.items():
        tasks.append(asyncio.create_task(water(k, v)))
    for task in tasks:
        await task


# set watering requirements for today based on ET0 data and area of a group
def init_properties():
    # area in m2
    with open("properties.json", "r") as area:
        properties = json.load(area)

    # evaporation in mm/day
    with open("PET_paramaribo.json", "r") as PETdata:
        year_day = datetime.now().utctimetuple()[7] + 1
        evaporation = json.load(PETdata)[year_day] 
    
    # water requirement in L
    for k, v in properties["groups"].items():
        properties["groups"][k]["requirement_left"] = evaporation * v["area"] * v["crop_factor"]
    return properties

    

properties = init_properties()
print(properties)

def hourly_water():
# assuming we water from 7 to 19.00, 12 waterings
    rain_last_h = rain_last_hour()
    cycles_left = 19 - datetime.now().hour
    timer = {}
    # remove rainfall from requirements. Also, did a mod that made rain count as 0.5 that of irrigation. 
    for k, v in properties["groups"].items():
        properties["groups"][k]["requirement_left"] = max(0,  v["requirement_left"] -   ( 0.5 * v["area"] * rain_last_h ))
        # time for a group = requirement left / cycles left / flowrate * 60 secs
        timer[k] = (properties["groups"][k]["requirement_left"] * 60 / cycles_left) / properties["flowrate"]
    print(timer)
    asyncio.run(water_groups(timer))
    for k, v in timer.items():
        properties["groups"][k]["requirement_left"] =  properties["groups"][k]["requirement_left"] - v

    

hourly_water()
print(properties)
hourly_water()
print(properties)



