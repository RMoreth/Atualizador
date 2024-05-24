# lista de 6 nomes
nomes = ["Lucas", "Ana", "Pedro", "Mariana", "João", "Carla"]

# usuario informa o índice que deseja alterar

indice = int(input("informe o indice que voce deseja alterar"))
indice -= 1

nomes[indice] = input("Informe o novo nome: ")

for v, nome in enumerate(nomes):
    print(f"Posição: {v+1}, nome: {nome} ")