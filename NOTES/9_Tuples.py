# Tuples - can store different types together
student = (["Alice", "Bob"], ["Math", "Science", "English"], 20, 'XYZ')

nam, sub, n, s = student # unpacking Tuple
print(nam[1])
print(sub[2])
print(n)
print(s)

student = ([2, 2], [2, 2, 2], 2, 2, 3) # Immutable, Duplicates allowed
print(len(student)) # no. of elements
print(student.count(2)) # occurences in tuple

my_tuple = (1, 2, 3)
new_tuple = my_tuple * 2 # repetition of the tuple elements
print(new_tuple)