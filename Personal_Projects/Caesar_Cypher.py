import string

while True:
    def caesar_cipher(text, shift, mode="encrypt"):
        alphabet = string.ascii_lowercase
        result_text = ""

        for char in text:
            if char.isalpha():
                is_upper = char.isupper()
                base = string.ascii_uppercase if is_upper else alphabet
                if mode == "decrypt":
                    new_char = base[(base.index(char.lower()) - shift) % 26]
                else:
                    new_char = base[(base.index(char.lower()) + shift) % 26]
                result_text += new_char.upper() if is_upper else new_char
            else:
                result_text += char

        return result_text

    mode = input("Do you want to encrypt or decrypt? (type 'encrypt' or 'decrypt'): ").strip().lower()
    text = input("Enter your text: ").lower()
    shift_value = int(input("Enter the shift value: "))

    result = caesar_cipher(text, shift_value, mode)
    print(f"{mode.capitalize()}ed Message:", result)
