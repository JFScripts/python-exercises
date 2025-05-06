def main():
    #Pedindo o input do usuario
    expression = input("Digite uma expressão (a + b):\n")

    #Descobrindo a operação desejada
    if expression.find("+") != -1:
        x, y = expression.split("+")
        print(float(x)+float(y))

    elif expression.find("-") != -1:
        x, y = expression.split("-")
        print(float(x)-float(y))

    elif expression.find("*") != -1:
        x, y = expression.split("*")
        print(float(x)*float(y))

    elif expression.find("/") != -1:
        x, y = expression.split("/")
        if y == "0": print("Impossivel dividir por Zero")
        else: print(float(x)/float(y))

    else:
        print("Erro: Operação não identificada")

main()