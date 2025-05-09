import emoji

def main():
    while True:
        #Controle do looping
        try:
            emoji_text = input("Digite o código de um emoji ou digite CTRL+D para encerrar o programa:\n")
        except EOFError:
            break
        #Convertendo para o emoji certo
        emoji_processado = emoji.emojize(emoji_text)

        #Conferindo se o Emoji existe e dando um feedback
        if emoji.is_emoji(emoji_processado):
            print(emoji_processado)
        else:
            print("Emoji não existe")

main()