import sys
import random
from pyfiglet import Figlet
def main():

    print(len(sys.argv))
    if len(sys.argv) == 1 or len(sys.argv) == 3:
        figlet = Figlet()
        frase = input("Digite uma frase:\n")
        if len(sys.argv) == 3:
            fonte_selecionada = sys.argv[2]
            figlet.setFont(font=fonte_selecionada)
        else:
            figlet.setFont(font=random.choice(figlet.getFonts()))
        print(figlet.font)
        print(figlet.renderText(frase))
    else:
        sys.exit()

main()