# O jogo vai se passar em uma floresta encantada onde um rapaz está perdido da floresta 
from types import EllipsisType


def introducao():
    print("Bem-vindo à Floresta Encantada!")
    print("A tua missão é sair da florsta encantada e tens que ir para a tua casa ")

Nome = ("José")
print(f"O do nome do teu jogador é {Nome}") 
print("encontras dois caminhos")
escolha = input("Queres seguir para a direita ou para a esquerda? (direita/esquerda)")
if escolha == "direita":
    print("Encontras uma mochila com uma lanterna e um arco flecha!")

if escolha == "esquerda":
    print("encontraste um buraco e caiste dentro , morreste")
    exit()


print("encontras outros dois  caminhos (direita ou esquerda) ")
escolha = input("Queres seguir para a direita ou para a esquerda? (direita/esquerda):")

if escolha == "direita":
    print("Encontras um monstro onde tens que lutar contra ele  ")
    print("Ganhaste ao mostro com rescompesa ganhaste um escudo")
    
if escolha == "esquerda":
    print("tem um zombie e morres !")
    print("Fim de jogo")
    print("O jogo terminou. Obrigado por jogar!")
    exit()

print("Encontras as dois ultimos caminhos da saida da floresta")
escolha = input("Queres ir para a (direita ou esquerda)")
if escolha == "direita":
    print("encontraste a saida da floresta e voltas para a casa ")
if escolha == "esquerda": 
    print("tem dragão e morres queimado")
    print("fim de jogo")
    print("O jogo terminou. Obrigado por jogar!")
    exit()

print("Conseguiste fugir da floresta !")
print("Fim de jogo")
exit()
continuar = True
while continuar:
# Código do jogo aqui
    resposta = input("Queres jogar de novo? (sim/não): ")
    if resposta.lower() != "sim":
        continuar = False           

