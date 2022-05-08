'''
Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

Input
The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

Output
Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.
'''

n = float(input())
ni = int(n)
fl = round((n-ni)*100)
fl = round(fl)
#print(fl)

cem = int(n/100)
cinq = int((n-cem*100)/50)
vinte = int((n-cem*100-cinq*50)/20)
dez = int((n-cem*100-cinq*50-vinte*20)/10)
cinco = int((n-cem*100-cinq*50-vinte*20-dez*10)/5)
dois = int((n-cem*100-cinq*50-vinte*20-dez*10-cinco*5)/2)
um = int(n-cem*100-cinq*50-vinte*20-dez*10-cinco*5-dois*2)
cinqc = int((fl)/50)
vintec = int((fl-cinqc*50)/25)
dezc = int((fl-cinqc*50-vintec*25)/10)
cincoc = int((fl-cinqc*50-vintec*25-dezc*10)/5)
umc = int(fl-cinqc*50-vintec*25-dezc*10-cincoc*5)

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(cem))
print('{} nota(s) de R$ 50.00'.format(cinq))
print('{} nota(s) de R$ 20.00'.format(vinte))
print('{} nota(s) de R$ 10.00'.format(dez))
print('{} nota(s) de R$ 5.00'.format(cinco))
print('{} nota(s) de R$ 2.00'.format(dois))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(um))
print('{} moeda(s) de R$ 0.50'.format(cinqc))
print('{} moeda(s) de R$ 0.25'.format(vintec))
print('{} moeda(s) de R$ 0.10'.format(dezc))
print('{} moeda(s) de R$ 0.05'.format(cincoc))
print('{} moeda(s) de R$ 0.01'.format(umc))

