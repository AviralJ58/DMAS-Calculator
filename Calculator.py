def modify():
    dig[i]=t
    del dig[i+1]
    del op[i]
eq=input("CALCULATOR\nEnter the equation involving +,-,*,/\n")
eq=eq+" "
a=0
dig=[]
op=[]
for i in eq:
    if i.isdigit():
        a=(a*10)+int(i)
    else:
        dig.append(a)
        a=0
        if i !=' ':
            op.append(i)
while len(dig)>1:
    if '/' in op:
        i=op.index('/')
        t=dig[i]/dig[i+1]
        modify()
    elif '*' in op:
        i=op.index('*')
        t=dig[i]*dig[i+1]
        modify()
    elif '+' in op:
        i=op.index('+')
        t=dig[i]+dig[i+1]
        modify()
    elif '-' in op:
        i=op.index('-')
        t=dig[i]-dig[i+1]
        modify()
print('Answer:',dig[0])
input('Press ENTER to exit.')
