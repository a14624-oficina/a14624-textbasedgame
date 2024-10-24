# O jogo vai se passar em uma floresta encantada onde um rapaz está perdido da floresta 
def introducao():
 print("Bem-vindo à Floresta Encantada!")
print("A tua missão é sair da florsta encantada e tens que ir para a tua casa ")

Nome = ("José:")
print("O do nome do teu jogador é José") 
print("encontras dois caminhos")
escolha = input("Queres seguir para a direita ou para a esquerda? (direita/esquerda): ")
if escolha == "direita":
    print("Encontras uma mochila com uma lanterna e um arco flexa!")
else:
    print("tem um zombie e morres !")
print("Fim de jogo")
