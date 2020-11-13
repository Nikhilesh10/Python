#----------FILES
fname = input('Enter file name')
fhand = open(fname)
        #OR
fhand = open('abc.txt')
fhand = open('abc.txt',r)

fhand = open('abc.txt')
for i in fhand :
    print(i)              #prints whole file line by line

#counting
for i in fhand :
    count = count + 1
print(count)

fhand = open('abc.txt')
var = fhand.read()

print(len(var))
print(var[3:20])

#searching
fhand = open('abc.txt')
for line in fhand :
    if line.startswith('From:')
    print(line)

for line in fhand :
    if nor 'xyz' in line :
        continue
    print(line)



#Write a program that prompts for a file name, then opens that file and reads
#through the file, and print the contents of the file in upper case.
#Use the file words.txt to produce the output below.

fname = input("Enter file name: ")
fhandle = open(fname)

for line in fhandle :
    line = line.rstrip()
    print(line.upper())


#Write a program that prompts for a file name, then opens that file and reads
#through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines
#and compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#when you are testing below enter mbox-short.txt as the file name.

fname = input("Enter a file name")
fhandle = open(fname)
count = 0
avg = 0
sum = 0

for line in fhandle :
    if not line.startswith('X-DSPAM-Confidence:') :
        continue
    count = count+1
    x = line[17:]
    print(x.strip())
    x = float (x)
    sum = sum +x

avg = sum/count
print(avg)
