## wrt a programm to reverse the string
"""s = input("Please entersome string:")
s1 = s.split()
print(s1[2],s1[1],s1[0])
print("OR METHOD:")
#######
a = input("Please enter some string:")
b = a.split()
reversedchar = reversed(b)
print(' '.join(reversedchar))

s = "hello nilesh koli"
s1 = s.split()
print(s1[-1::-1])

#write a program to find single word with max length
a = "python is a object oriented and interprited language."
longest = max(a.split(),key = len)
print("longest word is:",longest)
print("And its length is:",len(longest))

string = "hello nilesh koli, have nice day."
def largestword(s):
    print(s)
    s = sorted(s,key=len)
    print(s[-1])
    print(len(s[-1]))
largest = string.split()
print(largestword(largest))

#Write a Python program to print a tuple with string formatting.
t = (100, 200, 300)
print("this is tuple {0}".format(t)
s = input("enter the reversed string is:")
output = s.split()
print("reversed string is:", (output[::-1]))

s = input("enter the reversed string is:")
r = reversed(s)
output = ''.join(r)
print(output)

s = "nilesh"
output = ''
i = len(s)-1
while i>=0:
    output = output + s[i]
    i = i-1
print(output)

s = "python is very very easy"
l = s.split()
l1 = l[::-1]
output = ' '.join(l1)
print(output)
s = "hello nilesh koli"
s1 = s.split()
print(s1[-1::-1])

## write a program to reverse internal content of each word?
s = "python is very very easy"
l = s.split()
l1 = []
for i in l:
    l1.append(i[::-1])
output = ' '.join(l1)
print(output)

# write a program to reverse internal content of every second word present in the given string?
s = 'one two three four five six'
l = s.split()
i = 0
l1 = []
while i<len(l):
    if i % 2 == 0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i = i+1
output = ' '.join(l1)
print(l1)

#wrt a program to print character present at even and odd index seperately for given string
l = 'abcdefghijklmnopqrstuvwxyz'
i = 0
print('print character at even index')
while i<len(l):
    print(l[i])
    i = i+2
i = 1
print('print character at odd index')
while i<len(l):
    print(l[i])
    i = i+2

#wrt assume input string contain only alphabet symbols and digits wrt a program to sort character of the string first alphabet symbols followd by digit
s = 'B4A1D3'
alphabet = []
digit = []
for i in s:
    if i.isalpha():
        alphabet.append(i)
    else:
        digit.append(i)
output = ''.join(sorted(alphabet)+sorted(digit))
print(output)

## wrt a program for the following requirement?
#input = a4b3c2
#output = aaaabbbcc
s = 'a4b3c2'
output = ''
for i in s:
    if i.isalpha():
        x = i
    else:
        d = int(i)
        output = output + x*d
print(output)

#write a program for the following requirement?
#input = a4z2b3
#output = aaaabbbzz
s = 'a4z2b3'
target = ''
for i in s:
    if i.isalpha():
        x = i
    else:
        d=int(i)
        target=target+x*d
print(target)
print(''.join(sorted(target)))

#wrt a program for the following requirement?
#input = a4k3b2
#output = aeknbd
s = 'a4k3b2'
output = ''
for i in s:
    if i.isalpha():
        output = output + i
        x = i
    else:
        d = int(i)
        newc = chr(ord(x)+d)
        output = output + newc
print(output)

#wrt a programme to find the input is supplied to the proigramme
#input = Hello world practice makes prfect
#output= HELLO WORLD PRACTICE MAKES PERFECT
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

a = 'Hello world Practice makes perfect'
b = a.split(' ',2)
c = b[0]+' '+b[1],b[2]
for i in c:
    if i:
        i = i.upper()
    print(i)

a = 'Hello world Practice makes perfect'
b = a.split(' ',2)
c = b[0]+' '+b[1],b[2]
for i in c:
    if i:
        i = i.upper()
    print(i)

#INPUT:-
#hello world and practice makes perfect and hello world again
#OUTPUT:-
#again and hello makes perfect practice world
a ='hello world and practice makes perfect and hello world again'
b = a.split()
print(' '.join(sorted(set(b))))

#Write a program, which will find all such numbers between 1000 and 3000 (both included)
#such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on a single line.
a = []
for i in range (1000,3000):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        a.append(s)
print(",".join(a))

s = 'nilesh koli'
b = ''
i = len(s)-1
while i>=0:
    b = b + s[i]
    i = i -1
print(b)

s = 'nileshkoli'
def reverse (s):
    str = ''
    for i in s:
        str = i + str
    return str
print(reverse(s))

s = 'nilesh koli'
s1 = s.split()
print(s1[1],s1[0])

x = ["a", "b", "c", "d"]
print(x[:3] and x[:-1])
print(x[-3:] and x[1:])
print(x[-2:] and x[:])

#python program  to detect if two strings are anagrams
s1 = input('Enter first string:')
s2 = input('Enter second string:')
if (sorted(s1) == sorted (s2)):
    print('The string are anagrams.')
else:
    print('The string aren\'t anagrams.')

#Write a Python program to swap comma and dot in a string.
a = "324.54,23"
print(a.replace(',','COMMA').replace('.',',').replace('COMMA','.'))
"""
print(b)