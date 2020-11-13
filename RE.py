#REGULAR EXPRESSIONS
#Guide

#  ^         Matches begining of the line
#  $         Matches end of the line
#  .         Matches any character
#  \s        Matches whitespace
#  \S        Matches any non whitespace character
#  *         Repeats a character zero or more times
#  *?        Repeats a character zero or more times  (non-greedy)
#  +         Repeats a character one or more times
#  +?        Repeats a character one or more times  (non-greedy)
#  [aeiou]   Matches a single character in the listed set
#  [^XYZ]    Matches a single character not in the listed set
#  [a-z0-9]  The set of characters can include a range
#  (         Indicates where string extraction is to start
#  )         Indicates where string extraction is to end

#search() - if strings match, returns T/F
#findall()   - if strings match, returns the string.

import re
#using re.search
fh = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From: ',line) :        #re.search() instead of line.find()
        print(line)

fh = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From: ',line) :        #^ instead of startswith()
        print(line)
# ^X-\S+ :
#Extracts lines starting with 'X-',followed by one or more non space characters,
#then ending with a colon.

#EXTRACTING DATA
x = "My 2 favourite numbers are 10 and 11"
y = re.findall('[0-9]+',x)
print(y)
#op => ['2','10','11']
y = re.findall('[AEIOU]+',x)
#op => []

x = "From nikhilesh5475@gmail.com Wed Sep 2 15:52:55 2020"
y = re.findall('^From (\S+@\S+)', x)   #'()'indicate the portion to be extracted
print(y)
#op => nikhilesh5475@gmail.com

#Greedy matching
x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print(y)
#op => ['From: Using the :']

#Non-Greedy matching
x = 'From: Using the : character'
y = re.findall('^F.+:?',x)
print(y)
#op => ['From:']
