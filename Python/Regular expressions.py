##  REGULAR EXPRESSIONS  ##

## Def:- Its an expression and it is used to extract the required information from the input.
## re is the pre-defined module used in python regular expression.

# 1) match() function:- Its used to test the input string starts with specified pattern or not.

# 2) search() function:- Its ised to test the specified pattern is present or not.

# 3) findall() function:- Its used to find the duplicates for specified pattern.



import re

str="python and Java are the programming languages. "
res=re.match(r'python',str)
print(res)
