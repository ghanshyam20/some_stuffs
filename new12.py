import json


x={
    "name":"balen",
    "age":30,
    "married":True,
    "divorce":False,
    "children":("james","smith"),
    "pets":None,
    "cars":[
        {"model":"Bmw 230","speed":20},
        {"model":"Ford","speed":24}
    ]
}

# x is python object
y=json.dumps(x)
print(type(y))

# print(json.dumps(x,indent=4,sort_keys=True))



