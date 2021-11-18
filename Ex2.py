def potencia(a,b):
    r = a**b
    return r
n1 = int(input("Digite o valor de A: "))
n2 = int(input("Digite o valor de B: "))
func = potencia(n1,n2)
print(f"{n1}**{n2}= {func}")