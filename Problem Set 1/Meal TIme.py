def main():
    horario = input("Digite o Horário (hh:mm):\n")

    if 7 <= convert(horario) <= 8:
        print("Hora do Café da Manhã!")
    elif 12 <= convert(horario) <= 13:
        print("Hora do Almoço!")
    elif 18 <= convert(horario) <= 19:
        print("Hora da Janta!")
    else:
        print("Não é hora de comer...")


def convert(time):
    hora, minuto = str(time).split(":")
    hora = float(hora)
    minuto = float(minuto)
    return hora + (minuto/60)



if __name__ == "__main__":
    main()
