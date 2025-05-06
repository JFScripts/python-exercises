def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?\n")
    answer = answer.upper().replace(" ","-").strip()

    if answer == "42" or answer == "FORTY-TWO":
        print("YES")
    else:
        print("No...")

main()