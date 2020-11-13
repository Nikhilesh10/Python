#---------While loop

while True :
    line = input('> ')
    if line[0] == '#' :
        continue               #skips current iterations,jumps to next iteration
    elif line = 'done':
        break                  #immediately exits out of the loop
    print(line)

print('While Loop Done')

#---------For loop

for i in [5,4,3,2,1] :
    print(i)
