import math

def bins():
    #dictionary of ASCII letters to binary
    asc = {' ': '00100000', 'A': '01000001', 'B': '01000010', 'C': '01000011', 'D': '01000100', 'E': '01000101', 'F': '01000110', 'G': '01000111', 'H': '01001000', 'I': '01001001', 'J': '01001010', 'K': '01001011', 'L': '01001100', 'M': '01001101', 'N': '01001110', 'O': '01001111', 'P': '01010000', 'Q': '01010001', 'R': '01010010', 'S': '01010011', 'T': '01010100', 'U': '01010101', 'V': '01010110', 'W': '01010111', 'X': '01011000', 'Y': '01011001', 'Z': '01011010', 'a': '01100001', 'b': '01100010', 'c': '01100011', 'd': '01100100', 'e': '01100101', 'f': '01100110', 'g': '01100111', 'h': '01101000', 'i': '01101001', 'j': '01101010', 'k': '01101011', 'l': '01101100', 'm': '01101101', 'n': '01101110', 'o': '01101111', 'p': '01110000', 'q': '01110001', 'r': '01110010', 's': '01110011', 't': '01110100', 'u': '01110101', 'v': '01110110', 'w': '01110111', 'x': '01111000', 'y': '01111001', 'Z': '01111010', '!': '00100001', '?': '00111111'}

    useri = input("Enter a value to be converted to binary: ")

    #if the user inputs an integer or float, the input will be converted to a float, otherwise it is a string. 
    try:
        useri = float(useri)
        
        #intstring and floatstring will be appended to with the binary as the function executes
        intstring = []
        floatstring = []
        string = ''

        if useri > 0:
        
            def bina(bi):
            
                #This seperates the integer and float. The float is stored in flo, and the integer is stored in bi.
                flo = useri%1
                bi = useri - flo

                # returns the binary value of the integer. 
                while bi > 0:
                    r = bi%2
                    if r == 0:
                        bi = bi/2
                    elif r == 1:
                        bi = (bi-1)/2
                    #removes the decimal point from the result. 
                    r = math.floor(r)
                    #appends each iteration to the integer list.
                    intstring.append(r)
                #reverses the list order as the function opperates in reverse order. 
                intstring.reverse()
                #makes the integer list into a string for viewing purposes. 
                news = ''.join(map(str, intstring))

                #converts the float value into binary. 
                while flo != 0:
                    #converts float into binary by multiplying the float by 2, if the float is greater than or equal to 1, then 1 is subracted from the number until the number is zero, and the binary value of 1 is appended to the float list. 
                    if flo >= 1:
                        floatstring.append(1)
                        flo = (flo-1) * 2

                    #if the float is less than one then the result is multiplied by 2 again until it equals one, and a binary value of 0 is appended to the float list.
                    elif flo < 1:
                        floatstring.append(0)
                        flo = flo *2

                #appends a decimal point to the float list.
                floatstring.insert(0, '.')
                #converts the float list to a string for viewing. 
                new = ''.join(map(str, floatstring))
                print(news + new)
            bina(useri)

    # if the value entered by the user is not a number, then it is a string, so the ASCII to binary function is called. 
    except ValueError:
        def binasc(word):
            #word2 is appended to with the binary results of the word. 
            word2 = ''
            #The ASCII word is iterated through. 
            for letter in word:
                #if the ascii value is in the ascii to binary dictionary, then the binary value of the ascii key is appended to the word 2 list. 
                if letter in asc.keys(): 
                    word2 += asc.get(letter) + ' '
            print(word2)
            #print()
        binasc(useri)






