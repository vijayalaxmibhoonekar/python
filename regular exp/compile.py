import re
s1 = "riya and priya are best friends"
result = re.findall(r"\w",s1)
print(result)

import re
s1 =input("enter a string")
result = re.findall(r".",s1)
print(result)

import re
s1 = "I am student of college"
result = re.findall(r"\w+$",s1)
print(result)