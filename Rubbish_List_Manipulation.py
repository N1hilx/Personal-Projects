a = int(input(":"))
b = int(input(":"))
c = int(input(":"))
d = int(input(":"))

def lists(a,b,c,d):
    zoznam_1=[]
    for i in range(a+1):
        zoznam_1.append(i)
    zoznam_2=[]
    for i in range(a+1):
        zoznam_2.append(i+10)
    zoznam_2[len(zoznam_2)-1] = "KSI"
    if b in zoznam_2:
        zoznam_2.remove(b)
    zoznam_3=[]
    zoznam_3= list(reversed(zoznam_1[0:c]))
    zoznam_2 = zoznam_2 + (zoznam_1[0:c])
    zoznam_1[1] = d
    zoznam_1.sort()
    return (zoznam_1, zoznam_2, zoznam_3)
p = lists(a,b,c,d)
print(p)
            
