#-------Tuples
#*TUPLES ARE IMMUTABLE , CANT BE APPENDED OR ATLERED*
x = ('abc' , 'nik' , 'leo')
print(x[2])   #prints leo

y = ( 1 , 4 ,2)
print(max(y))

(x , y ,z) = ('hai' , 'hey' , 'hello')
print(y) #prints hey

#comparing tuples *The left most values are most significant*
(1 , 100) > (0 , 1000) #true
(1 , 2 , 3 ,4) > (1 ,2 ,1 ,100) #true
('nik' , 'abc' , 'xyz') > ('nik' , 'abc' , 'xxz') #true

#we can sort a dictionary with tuples
dict = {'nik' : 100 , 'abc' : 10 , 'leo' : 1000}
d.items()  #op=> dict_items([(nik,100) , (abc,10) , (leo,1000)])
sorted(dict.items())
#op=> [(abc,10),(leo,1000),(nik,100) ] #sorted acc. to keys

for k,v in sorted(dict.items()):
    print(k,v)

#Sort items by values instead of keys
dict = {'nik' : 100 , 'abc' : 10 , 'leo' : 1000}
tmp = list()                          #copy values to temporary list
for k,v in dict.items():
    tmp.append(v,k)

tmp = sorted(tmp)              #ascending
print(tmp)
tmp = sorted(tmp,Reverse=TRUE) #descending
print(tmp)
#op=> [(1000,leo),(100,nik),(10.abc) ] #sorted acc. to values

#---------------------Print top 10 most common words----------------------------
fname = input("Enter file name")
if len(fname) < 1 : fname = "mbox-short.txt"
fhandle = open(fname)
count = dict()

for line in fhandle :         #splitting into words,creating histogram for words
    words = line.split()
    for word in words :
        count[word] = count.get(word , 0) + 1

lst = list()
for key,val in count.items(): #storing vals,keys from dict in a list(as tuples).
    newtup = (val,key)
    lst.append(newtup)        #list has tuples in val,key order

lst = sorted(lst , Reverse=TRUE)

for val,key in lst[:10]:    #print top 10 by slicing
    print(key , val)        #print in key,val order

#-----------------ALTERNATIVE method to sort by values(LIST COMPREHENSION)
dict = {a:10 , b:1 , c:22}

print(sorted([v,k for k,v in dict.items()]))
#op=> [(1,b) , (10,a) , (22,c)]



#WAP to read the mbox-short.txt & figure out the distribution by hourof the day
#for each of the messages. You can pull the hour out from the 'From ' line by
#finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,sorted
#by hour as shown below.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hrs=dict()

for line in handle :
    if not line.startswith('From ') :
        continue
    line = line.split()
    line = line[5]
    line = line[0:2]
    hrs[line] = hrs.get(line,0) + 1

lst=list()
for value,count in hrs.items():
    lst.append((value,count))

lst.sort()
for value,count in lst:
    print(value,count)
