def main():
    nome_lista = []
    while True:
        try:
            cur_name = input("Digite um nome ou aperte CTRL+D para encerrar o programa: ")
        except EOFError:
            print("Adieu, adieu, to ",end="")
            for i in range(len(nome_lista)):
                if i == 0:
                    nome_formatado = nome_lista[i]
                elif i == len(nome_lista) - 1:
                    nome_formatado = " e " + nome_lista[i]
                else:
                    nome_formatado = ", " + nome_lista[i]

                print(nome_formatado, end="")
            break
        nome_lista.append(cur_name)



main()