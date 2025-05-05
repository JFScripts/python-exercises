def main():
    frase = input("Digite um frase:\n")

    frase = frase.replace(":)", "🙂")
    frase = frase.replace(":(", "🙁")

    print(frase)


main()