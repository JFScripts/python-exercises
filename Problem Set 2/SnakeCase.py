def main():
    camel = input("Digite o nome da variavel em Camel Case (nomeDaVariavel): ")
    print("A variavel em Snake Case (nome_da_variavel): ",end="")

    for i in range(len(camel)):
        if camel[i].isupper():
            print("_",end="")
            print(camel[i].lower(),end="")
        else:
            print(camel[i],end="")

main()