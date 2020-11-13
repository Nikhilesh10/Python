#Python Strings Examples

str1 = "Hello"
str2 = "Nik"
print(str1+str2)    #Concatenation

fruit = "banana"
print(fruit[1])    #Slicing , Indexing
print(fruit[1:3])
print(fruit[:4])
print(fruit[3:])

for letter in fruit :  #Looping through a string
    print(letter)

# 'in' as a logical operator

fruit = "banana"
'n' in fruit    #True
'ana' in fruit  #True
'z' in fruit    #False


#Built-in String library functions

fruit.lower()
fruit.capitalise()
fruit.find('na')
fruit.replace('ban','app')

fruit.lstrip()       #Strip whitespaces
fruit.rstrip()
fruit.strip()

fruit.startswith('b')
