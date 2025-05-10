import random

def main():
    nivel = get_level("Digite o nivel desejado (1;2;3)\n")
    generate_problems(nivel)

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


def generate_problems(dificuldade):
    dificuldade_max = (10 ** dificuldade)-1
    dificuldade_min = 10 ** (dificuldade - 1)
    x, y, s = [], [], []
    if dificuldade == 1:
        dificuldade_min = 0

    for i in range(10):
        x.append(random.randrange(dificuldade_min, dificuldade_max))
        y.append(random.randrange(dificuldade_min, dificuldade_max))
        s.append(x[i] + y[i])
        print(f"{x[i]} + {y[i]} = {s[i]}")

    ##print(f"Max {dificuldade_max}")
    ##print(f"Min {dificuldade_min}")



main()