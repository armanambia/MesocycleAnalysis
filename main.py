
import json

def load(filePath):
    file = open(filePath)
    obj = json.load(file)
    file.close()
    return obj

def process_day(cur):
    res = {}
    for ex in cur:
        for key,val in exercise_dict.items():
            if ex in val:
                res[key] = res.get(key, 0) + 1
                break
    return res

def process_week():
    res = {}
    res = dict.fromkeys(week_dict,'{}')
    for key in res.keys():
        res[key] = process_day(week_dict[key])
    return res

def calc_weekly_sets():
    res = dict.fromkeys(exercise_dict,0)
    for e in week_breakdown.values():
        res = {x: res.get(x,0) + e.get(x,0) for x in set(res).union(e)}
    return res

exercise_dict = load('assets\exercises.json')
for key,val in exercise_dict.items():
        exec(key + '=val')

week_dict = load('assets\week.json')
for key,val in week_dict.items():
        exec('day_' + key + '=val')

week_breakdown = process_week()
week_total = calc_weekly_sets()
print(week_total)