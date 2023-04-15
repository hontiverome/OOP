import pyfiglet, termcolor, time
Message = ""
KeyWord = ""
#Activity 2 No3 Pseudocode
def MainCode(Message, KeyWord):
    CipherText = ""
    KeyValues = [ord(j) - 65 for j in KeyWord]  # This block of code will convert the keyword to a corresponding letter value (0 - 25)
    Position = 0  # Letter to be converted, starting with 0
    for j in Message:
        # Convert current positional character to a corresponding letter value (0 - 25)
        LetterValue = ord(j) - 65
        # Modulo 26 to have a range of  0-25 only
        CipherValue = (LetterValue + KeyValues[Position]) % 26
        # Convert the  value back to a letter
        CipherCharacter = chr(CipherValue + 65)
        # Add cipher character/letter to the resulting cipher text
        CipherText += CipherCharacter
        # Add current position into the keyword (looping until program reaches the very last letter)
        Position = (Position + 1) % len(KeyWord)
    return CipherText

#Design purposes hehehe
def Results():
    Result = 'Here is your Cypher text:\n'
    for i in range(len(Result)):
        print(termcolor.colored(Result[i], 'green'), end='', flush=True)
        time.sleep(0.1)
def CreatedCypherText():
    Seperate= ' '.join(CipherText)
    print(termcolor.colored(pyfiglet.figlet_format(Seperate, font="alligator", justify="center", width=220), 'red'))
    print("or:\n")
    for i in range(len(Seperate)):
        print(termcolor.colored(f"{Seperate[i]}", 'red'), end='', flush=True)
        time.sleep(0.09)

  
# Execute the Main Program
Message = str(input("Enter the message.\n: "))
KeyWord = str(input("Enter the keyword.\n: "))
CipherText = MainCode(Message, KeyWord)
Results()
# Locally created function prints the output
CreatedCypherText()

#PRODUCE THE CIPHERTEXT OF THE FOLLOWING:
#Message: THISISTHELASTTASKHOORDAY
#Key: KNIGHTS

#BSCPE1-5
#HONTIVEROS, Jerome Andrei O.
