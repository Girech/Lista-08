func = lambda a, b, c, d: ((a+b+c+d)/2)

n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
n4 = int(input("Digite a quarta nota: "))

if((n1>=0 and n1<=4)or(n3>=0 and n3<=4)):
    if((n2>=0 and n2<=6)or(n4>=0 and n4<=6)):
        print(func(n1,n2,n3,n4))
    else:
        print("Digite um valor valido")
else:
    print("Digite um valor valido")
x = func(n1,n2,n3,n4)
if (x>=0 and x<=4.9):
    print(f"Media: {x} Nota: D")
if (x>=5 and x<=6.9):
    print(f"Media: {x} Nota: C")
if (x>=7 and x<=8.9):
    print(f"Media: {x} Nota: B")
if (x>=9 and x<=10):
    print(f"Media: {x} Nota: A")
