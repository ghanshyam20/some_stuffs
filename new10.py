import json
print(json.dumps({"name":"john","age":30}))  #dict
print(json.dumps(["apple","banana"])) #list
print(json.dumps(("1,2,3,4")))   #tuple
print(json.dumps("sanjeev"))  #string
print(json.dumps(45))  #integer value
print(json.dumps(34.5))  #float value
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

