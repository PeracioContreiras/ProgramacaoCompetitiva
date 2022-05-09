'''
Using the following table, write a program that reads a code and the amount of an item. After, print the value to pay. This is a very simple program with the only intention of practice of selection commands.

1, Cachorro Quente, 4.00
2, X-Salada, 4.50
3, X-Bacon, 5.00
4, Torrada simples, 2.00
5, Refrigerante, 1.50

Input
The input file contains two integer numbers X and Y. X is the product code and Y is the quantity of this item according to the above table.

Output
The output must be a message "Total: R$ " followed by the total value to be paid, with 2 digits after the decimal point.
'''

e1 = input().split()
x = e1[0]
y = int(e1[1])

l1 = ('1','Cachorro Quente', '4.00')
l2 = ('2', 'X-Salada', '4.50')
l3 = ('3', 'X-Bacon', '5.00')
l4 = ('4', 'Torrada simples', '2.00')
l5 = ('5', 'Refrigerante', '1.50')

if x == l1[0]: print('Total: R$ {:.2f}'.format(float(l1[2])*y))
if x == l2[0]: print('Total: R$ {:.2f}'.format(float(l2[2])*y))
if x == l3[0]: print('Total: R$ {:.2f}'.format(float(l3[2])*y))
if x == l4[0]: print('Total: R$ {:.2f}'.format(float(l4[2])*y))
if x == l5[0]: print('Total: R$ {:.2f}'.format(float(l5[2])*y))