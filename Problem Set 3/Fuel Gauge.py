def main():
    continuar = "1"
    while continuar != "0":
        #Atribuido o retorno da função pega_valor e passando o prompt que será mostrado
        combustivel = pegar_valor("Digite o valor do tanque de combustivel (X/Y):\n")

        #Printando para cada condição do tanque
        if combustivel <= 1:
            print("Tanque Vazio")
        elif combustivel >= 99:
            print("Tanque Cheio")
        else:
            print(f"O tanque está {combustivel}% cheio")
        continuar = input("Digite '0' Para encerrar | Pressione 'Enter' ou qualquer tecla para continuar\n")

def pegar_valor(prompt):
#Tentar até dar certo
    while True:
        try:
            valor = input(prompt).split("/") #Verificando se é inteiro
            try:
                if int(valor[0]) <= int(valor[1]): #Verificando se X é maior que Y
                    return (int(valor[0])/int(valor[1]))*100 #Convertendo em Porcentagem
                else:
#Dando Retorno para os possiveis erros
                    print("Impossivel ter mais combustivel que cabe no tanque")
            except ZeroDivisionError:
                print("Divisão por Zero")
        except ValueError:
            print("Precisa ser um número inteiro")

main()