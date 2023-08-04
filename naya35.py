import re
text="Our Nepal is Beautiful"
y=re.finditer("\s",text)


positions=[]

for match in y:
    positions.append(match.start())

if len(positions)>=1:
    print("The fist white space charater is located in position",positions[0])


if len(positions)>=2:
    print("The second white space character is located in position",positions[1])


else:
    print("The is no second white space character")


if len(positions)>=3:
    print("the third white space character is located in position",positions[2])

else:
    print("there is no third white space charater in the text")














