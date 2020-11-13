#-----------DICTIONARIES
#Eg : Creating a dicitonary #1
messi = dict()          #dictionary
messi['goals'] = 25     #key,value
messi['assists'] = 21
messi['dribbles'] = 6.0
print(messi)
messi['dribbles'] = messi['dribbles'] + 2.0 #mutable

#Creating a dictionary #2

leo = {'goals' : 50 , 'assists' : 18 , 'dribbles' : 7.0 }

#-------The get() method of Dictionaries
# get(key,default) returns value stored in the key...if the key isnt present..
# it returns a default value.

x = messi.get('goals' , 45) #returns 25(already exists) and stores in x
x = messi.get('trophies' , 2) #returns 2 and stored in x

#printing a dictionary
print(messi)
print(messi.key())              #prints the keys alone
print(messi.values())           #prints the values alone
print(list(messi))              #prints the dict() in the form of a list
print(messi.items())            #prints the dict() in the form of a tuple

for k,v in messi.items():         #looping with 2 iterable variables
    print(k,v)                  #prints each key and value as a tuple

#Eg : Program to create histogram and count no. of occurences of each name
count = dict()
names = ['Messi' , 'Ronaldo', 'Neymar' , 'Messi' , 'Neymar' , 'Suarez' ,'Messi']
for i in names :
    count[i] = count.get(i , 0) + 1
print("Count of each name", count)


#Write a program to read through the mbox-short.txt and figure out who has sent
#the greatest number of mail messages. The program looks for 'From ' lines and
#takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to
#a count of the number of times they appear in the file. After the dictionary is
#produced, the program reads through the dictionary using a maximum loop to find
#the most prolific committer.

fname = input("Enter file name")
if len(fname) < 1 : fname = "mbox-short.txt"
fhandle = open(fname)
names = dict()
l = list()
for line in fhandle :
    if not line.startswith('From ') :
        continue
    words = line.split()
    words.append(words[1])
for word in words :
    names[word] = names.get(word , 0) + 1

max_count = None
max_name = None

for k,v in names.items() :
    if max_count is None or v > max_count :
        max_count = v
        max_name = k

print(max_name , max_count)
