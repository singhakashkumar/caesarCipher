from caesarArt import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(plainText, shiftAmount, cipherDirection):
    caeserText = ''
    if cipherDirection == "decode":
                shiftAmount *= -1
    for character in plainText:
        if character in alphabet:
            position = alphabet.index(character)
            newPosition = (position+26+shiftAmount)%26
            caeserText += alphabet[newPosition]
        else:
            caeserText += character
    print(f"The {cipherDirection}d text is \"{caeserText}\"")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(plainText=text, shiftAmount= shift, cipherDirection= direction)
    restart = input("Enter 'yes' to restart, 'no' to terminate: \n")
    if restart == 'no':
        should_continue = False
        print("Goodbye")


