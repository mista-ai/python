import json

with open('text_7.txt', 'r', encoding='utf-8') as f:
    my_obj = [dict(), dict()]
    for line in f:
        line = line.split()
        my_obj[0][line[0]] = int(line[2]) - int(line[3])
    nonunprofitable = [profit for profit in my_obj[0].values() if profit >= 0]
    my_obj[1]["average_profit"] = sum(nonunprofitable) / len(nonunprofitable)
    with open('text_7.json', 'w', encoding='utf-8') as json_f:
        json.dump(my_obj, json_f, indent=4, ensure_ascii=False)
