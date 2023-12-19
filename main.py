
import json
import excel as e
from collections import OrderedDict

def load(filePath):
    file = open(filePath)
    obj = json.load(file)
    file.close()
    obj = json.loads(json.dumps(obj), object_pairs_hook=OrderedDict)
    return obj

def process_day(cur):
    res = OrderedDict.fromkeys(exercise_dict,0)
    for ex in cur:
        for key,val in exercise_dict.items():
            if ex in val:
                res[key] = res.get(key, 0) + 1
    return res

def process_week():
    res = OrderedDict.fromkeys(week_dict,'{}')
    for key in res.keys():
        res[key] = process_day(week_dict[key])
    return res

def calc_weekly_exercises():
    res = OrderedDict.fromkeys(exercise_dict,0)
    print(res)
    
    for e in week_breakdown.values():
        res = {x: res.get(x,0) + e.get(x,0) for x in res.keys()}
    return res


exercise_dict = load('assets\exercises.json')
for key,val in exercise_dict.items():
    exec(key + '=val')

week_dict = load('assets\week.json')
for key,val in week_dict.items():
    exec(str(key).replace(" ", "").replace("+","_") + '=val')

week_breakdown = process_week()
week_total = calc_weekly_exercises()

e.export(week_dict, week_breakdown, week_total)

print(week_breakdown)
print(week_total)