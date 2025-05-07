def main():
    frutas = {"maçã": "130",
              "abacate": "60",
              "banana": "110",
              "melão": "60",
              "toranja": "60",
              "uva": "60",
              "kiwi": "90",
              "limão": "16",
              "cereja": "100"}
    print("Escolha um Fruta:")

    for fruta in frutas:
        print(fruta)
    selecionada = str(input()).lower()

    print(f"A fruta selecionada tem {frutas[selecionada]} calorias")



main()