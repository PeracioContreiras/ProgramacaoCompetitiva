'''
Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's impossible to calculate the roots because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.

Input
Read 3 floating-point numbers (double) A, B and C.

Output
Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.
'''

numbs = input().split()

n1 = float(numbs[0])
n2 = float(numbs[1])
n3 = float(numbs[2])

delta = n2**2-4*n1*n3

if n1!=0 and delta>0:

    r1 = ((-n2+(delta**(1/2)))/(2*n1))
    r2 = ((-n2-(delta**(1/2)))/(2*n1))

    print('R1 = {}'.format(round(r1,5)))
    print('R2 = {}'.format(round(r2,5)))
else:
    print('Impossivel calcular')