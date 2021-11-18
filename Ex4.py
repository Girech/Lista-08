def ficha(a="Desconhecido",b=0):
    r = print(f"Nome: {a} Qt de gols: {b}")
    return r
nome = input("Digite o seu nome: ")
gols = int(input("Digite a quantidade de gols: "))
func = ficha(nome,gols)

