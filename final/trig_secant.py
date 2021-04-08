import math

#This function can be called in another program.
def trig():
    

    #i input determines which function the module will call. 
    i = input('To calculate the secant press 1, for cosecant press 2, for cotangent press 3: ')
    if i == '1':
        
        # q input determines if the user wants to find the secant/cosecant/cotangent with an angle or the sides. 
        q = input('To calculate the secant using the angle press 1, for sides press 2: ')

        if q == '1':

            #angle is passed to the function, this angle will then be converted to the secant/cosecant/cotangent 
            angle = float(input('Enter the angle: '))

            def secant(angle):
                r = 1/(math.cos(math.radians(angle)))
                print('The secant angle of %s degrees is: %s degrees' % (angle, r))
            secant(angle)
        

        elif q == '2':

            #if the user is using the sides to calculate the secant etc, then they will be asked to input the relevant sides which will then be passed to the function
            hyp = float(input('Enter the hypotenuse: '))
            adj = float(input('Enter the adjacent: '))

            def secant_sides(hyp,adj):
                r = hyp/adj
                print('The secant angle of the triangle with the hypotenuse of %s and the adjacent of %s is: %s degrees' % (hyp, adj, r))
            secant_sides(hyp,adj)


    elif i == '2':

        q = input('To calculate the cosecant using the angle press 1, for sides press 2: ')

        if q == '1':

            angle = float(input('Enter the angle: '))

            def cosecant(angle):
                r = 1/(math.sin(math.radians(angle)))
                print('The cosecant angle of %s degrees is: %s degrees' % (angle, r))
            cosecant(36.8)


        elif q == '2':

            hyp = float(input('Enter the hypotenuse: '))
            opp = float(input('Enter the opposite: '))

            def cosecant_sides(hyp, opp):
                r = hyp/opp
                print('The cosecant angle of the triangle with the hypotenuse of %s and the adjacent of %s is: %s degrees' % (hyp, opp, r))
            cosecant_sides(hyp,opp)

    elif i == '3':

        q = input('To calculate the cotangent using the angle press 1, for sides press 2: ')

        if q == '1':

            angle = float(input('Enter the angle: '))

            def cotangent(angle):
                r = 1/(math.tan(math.radians(angle)))
                print('The cotangent angle of %s degrees is: %s degrees' % (angle, r))
            cotangent(angle)


        elif   q == '2':
            adj = float(input('Enter the adjacent: '))
            opp = float(input('Enter the opposite: '))


            def cotangent_sides(adj, opp):
                r = adj/opp
                print('The cotangent angle of the triangle with the adjacent of %s and the opposite of %s is: %s degrees' % (adj, opp, r))
            cotangent_sides(adj,opp)

