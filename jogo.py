# O jogo vai se passar em uma floresta encantada onde um rapaz está perdido da floresta 
def introducao():
 print("Bem-vindo à Floresta Encantada!")
print("A tua missão é sair da florsta encantada e tens que ir para a tua casa ")

Nome = ("José:")
print("O do nome do teu jogador é José") 
print("encontras dois caminhos")
escolha = input("Queres seguir para a direita ou para a esquerda? (direita/esquerda)")
if escolha == "direita":
    print("Encontras uma mochila com uma lanterna e um arco flexa!")
else:
     print("encontras um lago cheio de crocodilos ")
     print("fim de jogo")



print("encontras outros dois  caminhos direita ou esquerda ")
escolha = input("Queres seguir para a direita ou para a esquerda? (direita/esquerda): ")

if escolha == "direita":
    print("Encontras um monstro onde tens que lutar contra ele  ")
    print("Ganhaste ao mostro com rescompesa ganhaste um escudo")
    mochila = []

    def adicionar_item(item):
        mochila.append(item)
        print(f"{item} foi escudo à tua mochila!")

    def remover_item(item):
        if item in mochila:
            mochila.remove(item)
            print(f"{item} foi removido da tua mochila.")

else:
 print("tem um zombie e morres !")
print("Fim de jogo")

print("Encontras as dois ultimos caminhos da saida da floresta")
escolha = input("Queres ir para a dirita ou esquerda")

