import string

def caesar_cipher():
    while True:
        try:
            alphabet = string.ascii_lowercase
            result = ""
            mode = input("Encrypt or decrypt? (type 'encrypt' or 'decrypt'): ").strip().lower()
            text = input("Enter text: ")
            shift = int(input("Shift value: "))

            for char in text:
                if char.isalpha():
                    base = string.ascii_uppercase if char.isupper() else alphabet
                    index = base.index(char.lower())
                    
                    if mode == "encrypt":
                        new_index = (index + shift) % 26
                    elif mode == "decrypt":
                        new_index = (index - shift) % 26
                    elif mode == "exit":
                        return
                    
                    result += base[new_index].upper() if char.isupper() else base[new_index]
                else:
                    result += char

            print(f"{mode.capitalize()}ed message: {result}")
        except ValueError:
            print("Shift value must be a number! Try again.")
