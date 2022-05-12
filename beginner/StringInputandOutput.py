'''
Your teacher would like to make a program with the following characteristics:

    Create 3 variables to store a phrase of up to 100 characters;
    Read a sentence for the first variable;
    Read a sentence for the second variable;
    Read a sentence for the third variable;
    Print the first variable read in step 2, the second variable read in step 3, the third variable read in step 4. Be sure to skip line;
    Print the first variable read in step 3, the second variable read in step 4, the third variable read in step 2. Be sure to skip line;
    Print the first variable you read in step 4, the second variable you read in step 2, the third variable you read in step 3. Be sure to skip line;
    Repeat procedure 5, printing only 10 characters of each variable.

Input
The input consists of several test files. Each test file has three rows. In the first line has a variable A that stores a phrase of up to 40 characters. In the second line has a variable B that stores a phrase of up to 40 characters. In the third line has a variable C that stores a phrase of up to 40 characters. As shown in the following input example.

Output
For each file in the input, you have an output file. The output file has four rows as described in items 5, 6, 7, and 8. As shown in the following output example.
'''

frase_1 = input()
frase_2 = input()
frase_3 = input()

print(frase_1 + frase_2 + frase_3)
print(frase_2 + frase_3 + frase_1)
print(frase_3 + frase_1 + frase_2)
print(frase_1[0:10] + frase_2[0:10] + frase_3[0:10])