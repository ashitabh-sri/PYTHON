# List - mutable in Python
num = [1, 2, 3, 4, 5] # just like array of C++
print(num[2]) # access by 0-based index

ele = [10, 20, 30, 40, 70, 60]
ele[4] = 50 # update by index
print(len(ele)) # gives the no. of elements

m = ["January", "February", "March", "April", "May", "June", "July"]
print(m[0:6])
print(m[1:5])
print(m[::2]) # slicing in List - start:end:step

numbers = [1, 2, 3, 4, 5]
a = int(input("Enter a Number: "))
numbers.append(a) # add element at end
print(numbers)

colors = ['red', 'green', 'blue']
a, b = input().split()
colors.insert(0, a) # index, element to be added
colors.insert(2, b)
print(colors)

random =  ['beetroot', 'horlicks', 'pineapple', 'peanuts', 'beetroot', 'horlicks', 'peanuts', 'apple']
a = input()
random.remove(a) # deletes the first occurence
print(random)

colors = ['black', 'blue', 'white', 'cyan', 'yellow', 'green']
a = int(input())
colors.pop() # deletes element at end
colors.pop(a) # deletes element by index, and return that element
print(colors)

list1 = ['Annihilate', 'Die for you', 'Am I dreaming', 'Burn the house down']
list2 = ['Hero', 'Maybe Man', 'Run', 'Enemy']
print(list2 + list1) # concatenation of lists

fruits = input().split() # store the inputs as list
print(fruits)

num = list(map(int, input().split())) # list of integers
print(num[::-1]) # prints in reverse order

import sys # for getsizeof
myNumbers = [10, 20, 30, 40, 50]
size_of_int = sys.getsizeof(myNumbers[2]) # returns size of variable
print(size_of_int)

N = input().split()
a = input()
if a in N: # performs linear search in list
    print("YES")
else:
    print("NO")