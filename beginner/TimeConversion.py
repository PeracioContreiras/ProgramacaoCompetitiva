'''
Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

Input
The input file contains an integer N.

Output
Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.
'''

n = int(input())
sec = n%60
hm = int(n/60)

if hm< 60:
    print('0:{}:{}'.format(hm, sec))
else:
    h = int(hm/60)
    min = hm%60
    print('{}:{}:{}'.format(h, min, sec))

