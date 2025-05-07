def main():
    moedas_total = 0
    while moedas_total < 50:
        moedas = 0
        moedas = int(input("Digite a Quantidade de Moedas Colocada (25, 10, 5):\n"))
        if moedas == 25 or moedas == 10 or moedas == 5:
            moedas_total += moedas

        else:
            print("\nValor da moeda Invalida\n")
        if 50-moedas_total > 0:
            print(f"Faltam {50 - moedas_total} centavos para comprar a Coca-Cola")

    print("Você Comprou uma Coca-Cola :)")
    if(moedas_total > 50):
        print(f"Devolvendo Troco de: {(50 - moedas_total)*-1} ")


main()