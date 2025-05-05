def main():
    massa = int(input("Digite a massa de um corpo em Kg:\n"))

    print(f"Sua energia em Joules é: {energia(massa)}J")

def energia(massa):
    return massa * ((3 * (10**8))**2)

main()