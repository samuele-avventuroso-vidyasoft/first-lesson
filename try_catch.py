import sys

def number():
    while True:
        try:
            number = int(input("Inserisci un number: "))
            print("Hai inserito il number:", number)
            break
        except ValueError:
            print("Errore: devi inserire un number valido. Riprova.")
    sys.exit(0)

if __name__ == "__main__":
    number()
