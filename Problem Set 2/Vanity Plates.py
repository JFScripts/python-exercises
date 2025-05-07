import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = str(s).upper()
    caracteres_especial = string.punctuation + " "
    primeiro = False

    if len(s) < 2 or len(s) > 6:
        print("Tamanho Invalido")
        return False
    elif not (s[0].isalpha() and s[1].isalpha()):
        print("Dois Caracteres tem que ser letra")
        return False
    elif s[len(s) - 1].isalpha():
        print("Ultimo Caracter não pode ser letra")
        return False
    for i in range(len(s)):
        if s[i] == "0" and primeiro == False:
            print("Primeiro Numero não pode ser 0")
            return False
            primeiro = True
        elif s[i].isnumeric() and primeiro == False:
            primeiro = True
        for j in range(len(caracteres_especial)):
            if s[i] == caracteres_especial[j]:
                print("Contem Caracter Especial")
                return False
    return True



main()
