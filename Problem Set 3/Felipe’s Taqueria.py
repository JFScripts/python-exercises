def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

    caixa(menu)


def caixa(menu):
    custo = 0
    while True:
        try:
            mostrar_menu(menu)
            pedido = input("Digite o item que deseja ou aperte CTRL+D para encerrar:\n").strip().title()
            custo += menu[pedido]
        except EOFError:
            print(f"\nValor total: ${custo}")
            break
        except KeyError:
            print("\nItem Inexistente\n")
        else:
            print(f"\nValor:${custo}\n")

def mostrar_menu(menu):
    for item in menu:
        print(f"{item} - ${menu[item]}")

main()