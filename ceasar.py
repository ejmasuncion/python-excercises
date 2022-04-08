# from ceasar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(code_direction, text_code, shift_amount):  
    end_text = ""
    if code_direction == "decode":
        shift_amount *= -1
    for x in text_code:
        if x not in alphabet:
            end_text += x
        else:
            code = alphabet.index(x)
            new_code = code + shift_amount
            end_text += alphabet[new_code]
    print(f"Here is the {direction}d result: {end_text}")


# print(logo)
restart = True
while restart == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26
    ceasar(code_direction = direction, text_code = text, shift_amount = shift)
    restart = input("Type 'yes' if you want to go again. Otherwise 'no': ")

    if restart == "no":
        restart = False
        print("Thanks. Goodbye")
    else:
        restart = True