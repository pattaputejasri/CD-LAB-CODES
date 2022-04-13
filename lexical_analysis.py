exp = input()
p = ""
for i in exp:
    if i in ' !@#$%^&*)(_-+={}|\:;<,>.?/\'':
        if p != "":
            print(p)
        p=""
    else:
        p+=i
if p != " ":
print(p)
