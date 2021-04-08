import math


asc = {' ': '00100000', 'A': '01000001', 'B': '01000010', 'C': '01000011', 'D': '01000100', 'E': '01000101', 'F': '01000110', 'G': '01000111', 'H': '01001000', 'I': '01001001', 'J': '01001010', 'K': '01001011', 'L': '01001100', 'M': '01001101', 'N': '01001110', 'O': '01001111', 'P': '01010000', 'Q': '01010001', 'R': '01010010', 'S': '01010011', 'T': '01010100', 'U': '01010101', 'V': '01010110', 'W': '01010111', 'X': '01011000', 'Y': '01011001', 'Z': '01011010', 'a': '01100001', 'b': '01100010', 'c': '01100011', 'd': '01100100', 'e': '01100101', 'f': '01100110', 'g': '01100111', 'h': '01101000', 'i': '01101001', 'j': '01101010', 'k': '01101011', 'l': '01101100', 'm': '01101101', 'n': '01101110', 'o': '01101111', 'p': '01110000', 'q': '01110001', 'r': '01110010', 's': '01110011', 't': '01110100', 'u': '01110101', 'v': '01110110', 'w': '01110111', 'x': '01111000', 'y': '01111001', 'Z': '01111010'}
useri = input("Enter:")

try:
    useri = float(useri)
    
    intstring = []
    floatstring = []
    string = ''

    if useri > 0:
    
        def bina(bi):
        
            flo = useri%1
            bi = useri - flo

            while bi > 0:
                r = bi%2
                if r == 0:
                    bi = bi/2
                elif r == 1:
                    bi = (bi-1)/2
                r = math.floor(r)
                intstring.append(r)
            intstring.reverse()
            news = ''.join(map(str, intstring))

            while flo != 0:
                if flo >= 1:
                    floatstring.append(1)
                    flo = (flo-1) * 2

                elif flo < 1:
                    floatstring.append(0)
                    flo = flo *2

            floatstring.insert(1, '.')
            floatstring.pop(0)
            #print(*li)
            new = ''.join(map(str, floatstring))
            print(news + new)
        bina(useri)

except ValueError:
    def binasc(word):
        word2 = ''
        for letter in word:
            
            if letter in asc.keys(): 
                word2 += asc.get(letter) + ' '
        print(word2)
        #print()
    binasc(useri)






