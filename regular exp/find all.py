import re
st = "book is from Sathya book of Python"
result = re.findall(r"book",st)
print(result)


print("==========================================")


import re
st=input("enter the string")
result=re.findall(r"book",st)
if result==None:
    print("book  found")
else:
    print(result)

print("=========================")


import re
st=input("enter string")
result=re.findall(r"Hai",st)
print(result)
print(len(result))
if result==[]:
    print("pattern not found")
else:
    print("pattern found")











