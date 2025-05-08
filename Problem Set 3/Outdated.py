def main():
    while True:
        data = input("Digite uma data (MM-DD-YYYY ou mes dia, ano)\n")
        if data[0].isnumeric():
            dataISO = ano_numerico(data)
        else:
            dataISO = ano_string(data)

        if dataISO:
            print(f"A data em formato ISO é {dataISO}")
            break


def ano_numerico(MDA):
    try:
        m, d, a = MDA.split("/")
        mes = int(m)
        dia = int(d)
        ano = int(a)
        if 1 <= mes <= 12 and 1 <= dia <= 31:
            return f"{ano:04d}-{mes:02d}-{dia:02d}"
    except ValueError:
        pass
    return None


def ano_string(ano):
    ano = ano.strip().title().replace(",", " ").split()
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    try:
        mes = meses.index(ano[0]) + 1
        dia = int(ano[1])
        ano_final = ano[2]
        data_formatada = f"{ano_final}-{mes:02d}-{dia:02d}"
        return data_formatada
    except (ValueError, IndexError):
       pass
    return None


main()