import re
st=input("enter the string")
result=re.search(r"book",st)
if result==None:
    print("match not found")
else:
    print("match  found")
