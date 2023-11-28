s = "Python je super! velmi super"

def upper(s):
    rozdel = s.split()
    for i in range(len(rozdel)):
        if i % 2 == 1:
            rozdel[i] = rozdel[i].upper()
    return " ".join(rozdel)
print(upper(s))
    





