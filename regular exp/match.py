import re
st="this is a book"
result=re.match(r"book",st)
print(result)

print("========================")

import re
st=input("enter the string")
result=re.match(r"book",st)
if result==None:
    print("match not found")
else:
    print("match  found")
print("========================")

import re
st = input("enter the string")
result = re.match(r"book",st)
print(result.start())
print(result.end())