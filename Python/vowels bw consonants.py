s='cdeofgiuhxae'
vowels='aeiou'
consonants=0
count=0
output=' '

for i in range(0,len(s)):                   # i=0     1       2         3           4           5           6           7           8           9           10          11              

    if s[i] not in vowels:      # s[0]=c        s[1]=d  s[2]=e  s[3]=o   s[4]=f    s[5]=g    s[6]=i    s[7]=u    s[8]=h
        consonants=1
    if consonants==1 and s[i] in vowels:
        count+=1                                                # cnt=1  cnt=2   
        output=output+s[i]                                  # 'e'           o
    elif count>1 and s[i] not in vowels:                                       # 'eo'
        print(output)
        count=0
        output=' '
        
    elif count<=1:
        count=0
        output=' '
   
