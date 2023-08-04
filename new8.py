import json

#JSON DATA
x='{"name":"sanjeev","age":30,"city":"New york"}'

#parse x:
y=json.loads(x)

# print(y)
print(y["age"])

# json data lai python object ma convert gareko ..


