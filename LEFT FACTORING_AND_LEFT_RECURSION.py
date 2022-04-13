s=input('X->')
l=s.split('|')
X1=''
for i in range(len(l[0])):
    if l[0][i]==l[1][i]:
        X1 = X1+l[0][i]
    else:
        break
X2='+'+X1
X3=X1+'+'
for i in range(len(l)):
    l[i]=l[i].replace(X1,'.')
    #X1='+'+X1
    l[i]=l[i].replace(X2,'.')
    #X1=X1+'+'
    l[i]=l[i].replace(X3,'.')
    #print(i)
X1=X1+'X\''
y1=''
for i in l:
    if '.' in i:
        i=i.replace('.','')
        y1=y1+i+'|'
    else:
        X1=X1+i
print('X->',X1)
print('X\'->',y1)
