#Write a program that repeatedly prompts a user for integer numbers until the
#user enters done. Once done is entered, print out the largest and smallest
#of the numbers. If the user enters anything other than a valid number catch it
#with a try/except and put out an appropriate message and ignore the number.



largest = None
smallest = None

while True :
    n = input('Enter a Number:')
    if n == 'done' :
        break
    try :
        n = int(n)
    except :
        print('Invalid Number')
        continue
    if largest == None :
        largest = n
    if smallest == None :
        smallest = n
    if n > largest :
        largest = n
    if n < smallest :
        smallest = n
print('Maximum is',largest)
print('Minimum is',smallest)
