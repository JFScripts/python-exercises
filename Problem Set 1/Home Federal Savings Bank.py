def main():
    greetings = input("Hello!\n")
    greetings = greetings.upper().strip()

    if greetings.__contains__("HELLO"):
        print("Sorry...You didn't win anything...")
    elif greetings.startswith("H"):
        print("Congratulations you won $20")
    else:
        print("Congratulations! You won $100")

main()