

numbers = [5, 20, 30, 35, 50]

insval = int(input('Enter the insertion value: '))

#flag variable that tells if insval has been inserted into the list
flag = 0

#This loop runs through numbers and sees if insval is less than or equal than the current value
#This is to find where it should be placed in the order
#if it is, the program inserts the number, turns flag to 1, and breaks the loop, so that insval is not inserted multiple times
for i in range(len(numbers)):
    if insval <= numbers[i]:
        numbers.insert(i, insval)
        flag = 1
        break

if flag == 0:
    numbers.append(insval)


print (numbers)
