def voto(a):
    r = 0
    if a >= 18:
        r = 1
        return r 
    if a >=16 and a <18 :
        r = 2
        return r 
    if a < 16:
        r = 3
        return r 
idade = int(input("Digite a sua idade:"))
func = voto(idade)
if func == 1:
    print("Voto obrigatório")
if func == 2:
    print("Voto opicional")

if func == 3:
    print("Voto negado")
