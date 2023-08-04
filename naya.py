#python RegEx

# A python RegEx or Regular Expression which is sequence of characters that form a search pattern.
# RegEx can be used to check if a string contains specified search pattern.

#RegEx Module

#python has a built in package called re, which can be used to used to work with regular expression.




# we can start using regular expression.


import re

txt="The rain in Nepal"

#chek if the string starts with "The" and ends with "Nepal"

x=re.search("^The.*Nepal$",txt)

if x:
    print("Yes! we have a match!")

else:
    print("No match")



#task=>Gautam Bhudda was born in nepal.








