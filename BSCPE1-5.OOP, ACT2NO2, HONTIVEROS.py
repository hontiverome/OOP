import pyfiglet, termcolor, time
#Activity 2 No2 Pseudocode
def MainCode():
    # Ask for input
    StrInput = str(input("What is your string?\n: "))
    StrOutput = ""  
    # Check each letter via loop
    for i in range(len(StrInput)):
        # If letter is *, change to a
        if StrInput[i] == "*":
            StrOutput += "a"
        # If letter is &, change to e
        elif StrInput[i] == "&":
            StrOutput += "e"
        # If letter is #, change to i
        elif StrInput[i] == "#":
            StrOutput += "i"
        # If letter is +, change to o
        elif StrInput[i] == "+":
            StrOutput += "o"
        # If letter is !, change to u
        elif StrInput[i] == "!":
            StrOutput += "u"
        # End loop
        else:
            StrOutput += StrInput[i]
    return StrOutput

#Design purposes hehehe
def Decrypted():
    result = "Here is the decrypted text:\n"
    for i in range(len(result)):
        print(termcolor.colored(result[i], 'green'), end='', flush=True)
        time.sleep(0.1)
def Results():
    Seperate= ' '.join(StrOutput)
    print(termcolor.colored(pyfiglet.figlet_format(StrOutput, font="smkeyboard", justify="center"), 'red'))
    print("or:\n")
    for i in range(len(Seperate)):
        print(termcolor.colored(f"{Seperate[i]}", 'red'), end='', flush=True)
        time.sleep(0.05)

# Execute the Main Program        
StrOutput=MainCode()
Decrypted()   
time.sleep(0.5)
# Locally created function prints the output
Results()

#Enter a string to decrypt: th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g.
#The Plain Text:  the quick brown fox jumps over the lazy dog.

#BSCPE1-5
#HONTIVEROS, Jerome Andrei O.