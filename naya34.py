"The rain in spain"
#yo ai kati patak aaako xa ? find garnu ?


# import re

# txt="The rain in spain"


#return a list containing every occurance of "ai"

#if no matches are found empty list is returned :
# y=re.findall("ai",txt)
# print(y)




#search function in RegEx
#The search() function searches the string for a match,and returns a Match Objects if there is a match.
#If there is more than on match only th e first occurance of the match will returned !

import re
y="Our Nepal is beautiful"

x=re.search("\s",y)


print("The first white-space character is located in position:",x.start())







