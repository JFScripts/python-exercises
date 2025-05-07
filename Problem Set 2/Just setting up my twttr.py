def main():
    tweeting = input("Digite o seu Tweet:\n")

    for i in range(len(tweeting)):
        if sem_vogal(tweeting[i]):
            print(tweeting[i], end="")


def sem_vogal(letra):
    letra = str(letra).lower()
    if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u":
        return True
    else:
        return False


main()