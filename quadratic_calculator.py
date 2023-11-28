a=float(input("Zadaj parameter a:"))
b=float(input("Zadaj parameter b:"))
c=float(input("Zadaj parameter c:"))
def solve(a: float, b: float, c: float) -> float:
    diskriminant=(b)**2 - 4*a*c
    if diskriminant<0:
        return None
    else:
        x1=(-b+(diskriminant)**0.5)/(2*a)
        x2=(-b-(diskriminant)**0.5)/(2*a)
    if x1>=x2:
        return x1
    else:
        return x2
v = solve(a,b,c)
print(v)
