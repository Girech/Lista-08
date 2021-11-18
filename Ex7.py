def media(a,b,c,d):
    if((a>=0 and a<=4)or(c>=0 and c<=4)):
        if((b>=0 and b<=6)or(d>=0 and d<=6)):
            r = (a+b)
            return r
        else:
            print("Digite um valor valido")
    else:
        print("Digite um valor valido")

n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
n4 = int(input("Digite a quarta nota: "))
func = media(n1,n2,n3,n4)
if (func>=0 and func<=4.9):
    print(f"Media: {func} Nota: D")
if (func>=5 and func<=6.9):
    print(f"Media: {func} Nota: C")
if (func>=7 and func<=8.9):
    print(f"Media: {func} Nota: B")
if (func>=9 and func<=10):
    print(f"Media: {func} Nota: A")
        
