alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(direction,text,shift):
    display=""
        # for letter in text:
        #  shift_position=alphabet.index(letter)-shift
        #  display+=alphabet[shift_position]
        # print("The Decoded Message is:",display)
    for letter in text:
        if letter not in alphabet:
            display+=letter
        else:
         if direction=="decode":
            shift*=-1

         shift_position=alphabet.index(letter)+shift
         new_index=shift_position%26
         display+=alphabet[new_index]
    print(f"The {direction}d text is:",display)

play_again=True
while play_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher(direction,text,shift)
    play=input("To Continue type y or else n:\n").lower()
    if play=="n":
        play_again=False
        print("Thank You")
    



