#--------------LISTS
#eg :
num = [1 , 5 ,10 , 15]
9 in num   #false
9 not in num #true
5 in num #true

football = ['Messi' , 'Neymar' , 'Suarez']
xyz = ['Messi' , 10, 91, 100.1 , [9,11]] #can contain all variable types

for i in xyz :
    print(i)

football[1] = 'Neymar Jr.' #Lists are Mutable
print(len(football))       #3
#print(range(football))     #[0 , 1 , 2]

#------building from scratch
futbol = list()
futbol.append('Ronaldinho')
futbol.append('Iniesta')
futbol.append('Xavi')

#------concatenate lists
barca = football + futbol
print(barca)
print(barca[1:3])
print(barca[4:5])
print(barca[3:])
print(barca[:3])
barca.sort()
print(barca)

#------built-in func
numbers = [1,5,10,4,6,2,3]
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(len(numbers))

#------print average of a bunch of numbers
x = list()

while True :
    a = input('Enter numbers')
    if a == 'done' :
        break
    a = float(a)
    x.append(a)

print(sum(x)/len(x))

#---------string to list

str = "Barcelona Liverpool BVB"
clubs = str.split()
print(clubs)    #[Barcelona , Liverpool , BVB]

str = "Barcelona;Liverpool;BVB"
club = str.split(';')
print(club)



#Open the file mbox-short.txt and read it line by line. When you find a line
#that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the
#line (i.e. the entire address of the person who sent the message).
#Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
l = list()

for line in fh :
    if not line.startswith('From ') :
        continue
    l = line.split()
    print(l[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
