import json

x={
    "name":"hariyo",
    "age":26,
    "married":False,
    "children":["hash","purple hedge","hemp"],
    "pets":None,
    "cars":[
        {"model":"BMW 230","mpg":45},
        {"model":"Himalay Hemp","mpg":25},
    ]
}

#convert into JSON:
y=json.dumps(x)

print(y)