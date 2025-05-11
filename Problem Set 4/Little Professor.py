import random

def main():
    # Quantidade de problemas gerados
    desafios = 10
    vida = 3
    pontos = 0
    # Pegando o nivel
    while vida > 0:
        nivel = get_level("Digite o nivel desejado (1;2;3)\n")
        print(f"Vida: {vida}\nPontos: {pontos}\n")
        # Calculando a dificuldade e retornando para um lista
        dificuldade = calculate_dificulty(nivel)

        # Gerando dois Valores com o intervalo da dificuldade
        x = generate_numbers(dificuldade[1], dificuldade[0], desafios) #Max - Min
        y = generate_numbers(dificuldade[1], dificuldade[0], desafios) #Max - Min

        # Calcular as soluções para cada soma
        pontos_ganho, vida = answers(x, y, desafios, vida)
        pontos += pontos_ganho
    print(f"Fim de jogo\nPontuação total: {pontos}")


def get_level(Prompt):
    while True:
        try:
            level = int(input(Prompt))
        except ValueError:
            print("O nivel precisa ser um numero inteiro")
        else:
            if 0 < level <= 3 :
                return level
            else:
                print("Escolha um nivel entre 1;2;3")


def calculate_dificulty(escolha):
    dificuldade = [9, 0]    #Padrão
    dificuldade[0] = (10 ** escolha) - 1 #Maximo
    dificuldade[1] = 10 ** (escolha - 1) #Minimo
    if escolha == 1:
        dificuldade[1] = 0
    return dificuldade

def generate_numbers(dificuldade_min, dificuldade_max, size):
    n = []
    for i in range(size):
        n.append(random.randrange(dificuldade_min, dificuldade_max))

    return n

def answers(n1, n2,size, lives):
    curDesafio = 0
    while lives > 0:
        if curDesafio == size:
            print(f"Parabens você ganhou esse nivel\nVoce ganhou {curDesafio} pontos")
            return curDesafio, lives
        print(f"{(curDesafio)+1:02d}) ", end="")
        try:
            tentativa = int(input(f"{n1[curDesafio]} + {n2[curDesafio]} = "))
        except ValueError:
            lives -= 1
            print(f"Resposta Errada\nVida:{lives}")
        else:
            if tentativa == (n1[curDesafio] + n2[curDesafio]):
                curDesafio += 1
            else:
                lives -= 1
                print(f"Resposta Errada\nVida: {lives}")
    return curDesafio, lives



main()