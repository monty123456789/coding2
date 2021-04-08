import math

#This function can be called in another program.
def trig():
    


    #i input determines which function the module will call. 
    i = input('To calculate the secant press 1, for cosecant press 2, for cotangent press 3: ')
    #j input determines if function will call inverse or normal
    j = input('To calculate the inverse press 1, otherwise press 2: ')


    types = ''
    #b will be updated with the relevant math method depending on user input
    b = math.cos
    side1 = ''
    side2 = ''

    #These if statements check both which function the user calls, and wheter they are calling the inverse of the function, and updates the variables accordingly. 
    if i == '1' and j == '2':
        types = 'secant'
        b = math.cos

        side1 = 'hypotenuse'
        side2 = 'adjacent'

    elif i == '1' and j == '1':
        types = 'secant'
        b = math.acos

        side1 = 'hypotenuse'
        side2 = 'adjacent'


    elif i == '2' and j == '2':
        types = 'cosecant'
        b = math.sin

        side1 = 'hypotenuse'
        side2 = 'opposite'

    elif i == '2' and j == '1':
        types = 'cosecant'
        b = math.asin

        side1 = 'hypotenuse'
        side2 = 'opposite'


    elif i == '3' and j == '2':
        types = 'cotangent'
        b = math.tan

        side1 = 'adjacent'
        side2 = 'opposite'


    elif i == '3' and j == '1':
        types = 'cotangent'
        b = math.atan

        side1 = 'adjacent'
        side2 = 'opposite'
     
        
        # q input determines if the user wants to find the secant/cosecant/cotangent with an angle or the sides. 
    q = input('To calculate the %s using the angle press 1, for sides press 2: ' % (types))

    if q == '1':

            #angle is passed to the function, this angle will then be converted to the secant/cosecant/cotangent 
        angle = float(input('Enter the angle: '))


        def secant(angle):
            r = 0
            inv = ''
            #If the user inputs 2 they don't want the inverse, so the normal function method is executed. 
            if j == '2':
                r = (1/(b(math.radians(angle))))
                inv = ''
            elif j == '1':
                r = (b(1/angle)) * 57.295779513
                inv = 'inverse of the '

            print('The %s %s angle of %s degrees is: %s degrees' % (inv, types, angle, r))
        secant(angle)
        

    elif q == '2':

            #if the user is using the sides to calculate the secant etc, then they will be asked to input the relevant sides which will then be passed to the function
        first = float(input('Enter the %s: ' % (side1)))
        second = float(input('Enter the %s: ' %(side2)))

        def secant_sides(first,second):
            if j == '2':
                r = first/second
            #If the user calls for the inverse, the angle must first  be determined before  the inverse can  be returned. 
            elif j == '1':
                a = second/first
                angle = b(a) * 57.295779513
                r = (b(1/angle)) * 57.295779513
                inv = 'inverse of the'

            print('The %s %s angle of the triangle with the %s of %s and the %s of %s = %s degrees' % (inv, types, first, side1, second, side2, r))
        secant_sides(first,second)


trig()
