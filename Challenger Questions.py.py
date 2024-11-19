''' Challenger Question - Brain Teaser '''


print()
print()
print('1. Challenger Question - Brain Teaser ')
print()

# 1 ---

print('1. Printing a pattern of Numbers')
print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,i,end=' ')
    print()

print()
print()


# 2 ---

print('2. Printing a pattern of Numbers')
print()

for i in range(1,6):
    for j in range(1,i+1):
        print(i,j,end=' ')
    print()
print()
print()



print()
print()
print()
print()

print('-------------------------------  Ch-4- Data Handling  ----------------------------------------')
print()
print()
print()
print()



#3 ----
print('3. Generalise Coding to Check for Prime Number')
print()

N=int(input('Enter any Integer to Check for Prime Number - '))
f=0
print()

if N>0:     # for positive integers only
    for i in range(2,N//2+1):
        if N%i==0:
            f=f+1
            break
        
    if f==0:
        print('1. Prime Number ')
    else:
        print('2. Not a Prime Number ')

else:     # for n<1 or for negative numbers and zero
    print(' 3. Not a Prime Number ')
                
print()
print()




# 4 ---

print('4. Generalise Coding to Print All Prime Number upto given input')
print()

n=int(input('Enter  upto which number All Prime Numbers are to be printed - '))
print()

for i in range(2,n+1):
    f=0
    for j in range(2,i//2+1):
        if i%j==0:
            f=f+1
            break
        
    if f==0:
        print(i,end=' ')
    
                
print()
print()



# 5 ---

print('5. Generalise Coding to check for Palindrome Number ')
print()

n=int(input('Enter any integer to check for Armstrong Number - '))
n1=n
s=0

while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if n1==s:
    print('Palindrome Number ')
else:
    print('Not a Palindrome Number ')
    
print()
print()






# 6 ---

print('6. Generalise Coding to Print All Palindrome Number upto given input')
print()

a=int(input('Enter upto which number All Palindrome Numbers are to be printed - '))
print()
for i in range(0,a+1):
    n=i
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if i==s:
        print(i,end=' ')
    else:
        pass
print()
print()




# 7 ---

print('7. Generalise Coding to check for Armstrong Number ')
print()

n=int(input('Enter any integer to check for Armstrong Number - '))
n1=n
s=0
print()

while n>0:
    r=n%10
    s=s+r**3
    n=n//10
if n1==s:
    print('Armstrong Number ')
else:
    print('Not a Armstrong Number ')


print()
print()



# 8 ---

print('8. Generalise Coding to Print All Armstrong Number between 0 to 1000 or all two digit and three digit armstrong number only')
print()

for i in range(0 ,1001):
    n=i
    s=0
    while n>0:
        r=n%10
        s=s+r**3
        n=n//10
    if i==s:
        print(i,end=' ')

print()
print()




# 9 ---

print('9. Generalise Coding to Print All Four Armstrong Number only')
print()

for i in range(1000,10000):
    n=i
    s=0
    while i>0:
        r=i%10
        s=s+r**4
        i=i//10
    if n==s:
        print(n,end=' ')

print()
print()





# 10 ---

print('10. Generalise Coding to Print All Five Armstrong Number only')
print()

for i in range(10000,100000):
    n=i
    s=0
    while i>0:
        r=i%10
        s=s+r**5
        i=i//10
    if n==s:
        print(n,end=' ')

print()
print()






# 11 ---

print('11. Generalise Coding to Check for Perfect Number')
print()

N=int(input('Enter any Integer to Check for Perfect Number '))
A=N
s=0
for i in range(1,N//2+1):
    if N%i==0:
        s=s+i
        
if A==s:
    print('Perfect Number ')
else:
    print('Not a Perfect Number ')

print()
print()






# 12 ---

print('12. Generalise Coding to Print All Perfect Number upto given input')
print()

N=int(input('Enter upto which number All Perfect Numbers are to be printed - '))
print()


for j in range(1,N+1):
    n=j
    s=0
    for i in range(1,j//2+1):
        if j%i==0:
            s=s+i
    if j==s:
        print(j,end=' ')
        
print()
print()





# 13 ---

print('13. Printing Pingala Series or Fibonacci Series ')
print()

A=0
B=1
N=int(input('Enter number of terms upto which the Pingala or fibonacci series is to be printed - '))
print()

if N>0:
    print(A,B,end=' ')

    for i in range(1,N-1):
        C=A+B
        print(C,end=' ')
        A=B
        B=C
else:
    print('Numbers of terms should be positive ')
    
print()
print()



# 14 ---

print('14. Printing Factorial of Whole Numbers')
print()

N=int(input('Enter any Whole Number to print its factorial- '))
f=1
print()

if N>=0:
    for i in range(1,N+1):
        f=f*i
    print('Factorial of ',N,'=',f)
        
else:
    print('Accepting Whole Numbers only to print its factorial ')
    
print()
print()




# 15 ---

print('15. Coding for the addition of the given series ')
print()

print(' x^1/1 + x^2/2 + x^3/3 + ------------------ + x^n/n ')
print()

x=int(input('Enter any integer - '))
n=int(input('Enter number of terms - '))
a=0
print()
for i in range(1,n+1):
    a= a + (x**i)/i
print('Result of the given information in the series = ',a)
    
print()
print()




# 16 ---

print('16. Coding for the addition of the given series ')
print()

print(' x^1/1! + x^2/2! + x^3/3! + ------------------ + x^n/n! ')
print()

x=int(input('Enter any integer - '))
n=int(input('Enter number of terms - '))
s=0
print()
for i in range(1,n+1):
    d=1
    for k in range(1,i+1):
        d= d*k
    s= s + (x**i)/d
print('Result of the given information in the series = ',s)
    
print()
print()


print()
print()
print()
print()

print('-------------------------------  Ch-5- String  ----------------------------------------')
print()
print()
print()
print()



# 17 ---

print('17. Enter any string containing odd number of characters to form triangle pattern ')
print()


A=input('Enter any string containing odd number of characters to form triangle pattern - ')
print()
p=len(A)
a=(p+3)//2

if p%2!=0:
    for i in range(1,a):
        for j in range(1,a-i):
            print(' ',end=' ')
        for k in range(0,i*2-1):
            print(A[k],end=' ')
        print()
        
else:
    print('String Does not contain odd number of characters')

print()
print()





# 18. ---

print('18 .To receive any string and check for Palindrome String ')
print()



s=input('Enter any string to check for Palindrome String - ')
s1=s[::-1]

if s==s1:
    print('Palindrome String')
else:
    print('Not a Palindrome String')


print()
print()
print()





# 19. ---

print('19. To receive any string and count upper case , lower case , digits , space character and special characters present in the provided string ')
print()

a=input('Enter any string - ')
u=0
l=0
d=0
s=0
sc=0

for i in a :
    if i.isupper():
        u=u+1
    elif i.islower():
        l=l+1
    elif i.isdigit():
        d=d+1
    elif i.isspace():
        s=s+1
    else:
        sc=sc+1

print('Upper Case Character = ',u)
print('Lower Case Character = ',l)
print('Numeric or Digit Character = ',d)
print('Space Character = ',s)
print('Special Character = ',sc)




# 20 ---

print('''20. Replacing vowels in the string with '*' character - ''')
print()

s=input('Enter any string - ')
s1=''
print()
print('''Replacing vowels in the string with '*' character - ''',end='')
      
for i in s:
    if i in 'aeiouAEIOU':
        s1=s1+'*'
    else:
        s1=s1+i

print(s1)




# 21 ---

print('''21. Receiving a text and printing biggest word from the text- ''')
print()

s=input('Enter any string - ')
large=0
p=s.split()
print()
      
for i in p:
    if len(i)>large:
        large=len(i)
        s1=i

print('Largest Word - ',s1)


print()
print()


















