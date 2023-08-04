#python
#history features
#python application
#vairable
#data types
#python keyword
#operators
#comments
#python if else
#python Loops
#Python for Loops
#python break
# while loop
#python pass
#python string
#python list
#python tuple
#python dict
#python set
#python date
#pyhton math
#numpy
#iterator
#python oops
#minor projects=>calculator,small banking system,gui clock,library management system.

#json=>javascript object notation
# it is a popular data format for online data exchange.Json is best for formatting data between client and  server.
#it is  the most efficient method for exchanging data and is simple to master it.

#JSON primarily supports the following six forms of data.
#string
#Number
#Boolean
#Null
#Object
#Array


# my_data={"name":"nepal","address":"asia","age":67,"language":"nepali"}
# print(type(my_data))

import json

#example of json data


json_data='''
{
"name":"Json smith",
"age":30,
"city":"New york"
}
'''

#parsing json data
data=json.loads(json_data)


# Accessing Json Values

name=data['name']
age=data['age']
city=data['city']

#modifying json values

data['age']=31

#converting python object to json string


modified_json=json.dumps(data,indent=4)

#printing the results

print(f"Name:{name}")
print(f"Age:{age}")
print(f"City:{city}")
print(f"MODIFIED JSON:{modified_json}")










