def main():
    compras = {}
    print("Digite a lista de compras ou pressione CTRL+D para encerrar")
    while True:
        try:
            item = input().strip().upper()
            compras[item] = compras.get(item, 0)+1
        except EOFError:
            for produto in sorted(compras):
                print(f"{compras[produto]} {produto}")
            break



main()