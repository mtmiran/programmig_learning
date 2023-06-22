import art


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caeser(plain_text, shift_amount, cipher_direction):
    cipher_text = ""

    for letter in plain_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = (position + shift_amount) % 26
        elif cipher_direction == "decode":
            new_position = (position - shift_amount) % 26
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The {direction}d text is {cipher_text}")

print(art.logo)


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser(plain_text=text, shift_amount=shift, direction=direction)

    result = input("Type, 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")