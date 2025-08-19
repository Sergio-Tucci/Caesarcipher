import art #import visual art

print(art.logo) #print logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #letter from alphabet

def caesar(original_text, shift_amount, encode_or_decode): # function to encode or decode the text
    output_text = "" # output text after swap letters
    if encode_or_decode == "decode": # check if user chose decoding
        shift_amount *= -1 # to turn shift number into negative, in this case we will go backwards through the letter in alphabet

    for letter in original_text: # for loop to go through an original text

        if letter not in alphabet: # check if a letter is not in alphabet that means it's space, number or special caracteres.
            output_text += letter #if it's not a letter, it will push the item (can be space number or special caracteres.)
        else: #in this case, its alphabet letter
            shifted_position = alphabet.index(letter) + shift_amount # take the original index of alphabet and add the numbers of shifts added by the user
            shifted_position %= len(alphabet) # use the rest of the division from alphabet to make sure when it goes further letter z, the code doesn't break.
            output_text += alphabet[shifted_position] # variable will accumulate the letters to form new text
    print(f"Here is the {encode_or_decode}d result: {output_text}") # print the result of the function


should_continue = True # variable receives boolean, it will be used for leaving while loop.

while should_continue: # while loop keeps the program running

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower() #variable to store the direction we will swap the letters to encrypt or decrypt the text.
    text = input("Type your message:\n").lower() # user inserts the text wanted
    shift = int(input("Type the shift number:\n")) # number of steps we will move to pick a letter in the alphabet

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction) # call the function

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower() # variable to check if user wants to continue running the program
    if restart == "no": # negative answer from user which means not continue running program
        should_continue = False # change variable value to False leaving while loop
        print("Goodbye") # print goodbye to warn user the program was terminated.