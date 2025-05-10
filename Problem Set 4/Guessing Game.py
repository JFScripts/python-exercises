import random
def main():
    intervalo_max = get_input("Digite um Número: ", "Digite um Número Inteiro")
    pontos = 0
    numero_escolhido = random.randrange(1, intervalo_max)
    while True:
        try:
            chute = int(input("Adivinhe o número gerado ou aperte CTRL+D para encerrar o programa:\n"))
        except ValueError:
            print("Digite um Número Inteiro!")
        except EOFError:
            print(f"O número Escolhido era {numero_escolhido}")
            break
        else:
            if chute == numero_escolhido:
                print(f"Parabens! Você acertou em {pontos} tentativas!")
                break
            elif chute < numero_escolhido:
                print("Numero Muito Pequeno")
            elif chute > numero_escolhido:
                print("Numero Muito Grande")
            pontos += 1


def get_input(prompt, e_feedback):
    while True:
        try:
            escolha = int(input(prompt))
            if escolha > 1:
                return escolha
        except ValueError:
            print(e_feedback)



main()