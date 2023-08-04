#python object lai json string ma convert garna lageko

import json


#a python object dict

x={
    "name":"elon",
    "age":54,
    "city":"New York"
}


#convert python object to Json;

y=json.dumps(x)

#the result is a json string
print(y)



