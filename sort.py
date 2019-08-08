begin = open('begin.txt','r')
digit = open('digit.txt','w')
alpha = open('alpha.txt','w')
code = open('code.txt','w')
countnum,countalpha,countcode = 0,0,0
s = begin.read().split()
for i in range(len(s)):
    if s[i].isdigit() == True and s[i].isalpha() == False:
        digit.write(s[i])
        digit.write('\n')
        countnum += 1
    elif s[i].isalpha() == True and s[i].isdigit() == False:
        alpha.write(s[i])
        alpha.write('\n')
        countalpha += 1   
    else:
        code.write(s[i])
        code.write('\n')
        countcode += 1
alpha.write(str(countalpha))
digit.write(str(countnum))
code.write(str(countcode))
begin.close()
digit.close()
alpha.close()
code.close()

