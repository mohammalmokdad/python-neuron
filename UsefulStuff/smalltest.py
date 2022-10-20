strs = ["a"]

length=len(strs)
if strs[0]=='':
    b=''
else:
    cont = True
    i=0
    vec=range(0,length,1)
    b=''
    while cont == True:
        if len(strs[0])>0:
            if len(strs[0])>i:
                a=strs[0][i]
                for j in vec:
                    if len(strs[j])>i:
                        if a!=strs[j][i]:

                            cont=False
                    else:
                        cont=False
                if cont==True:
                    i=i+1
                    b=b+a
            else:
                cont=False
        else:
            b=''
print(b)