# Assigning String
x = "Hello"
y = "World"
print(x + " " + y) # Concatenation

s = "tenet"
print(s * 100) # Repetition

txt = "NumeroTres"
length = len(txt) # gives the no. of characters
print(length)

string = 'Am I DreAmIng'
small = string.lower() # converts all to small letters
capital = string.upper() # converts all to capital letters
print(small)
print(capital)

word = "Progromming"
print(word[1])
print(word[-2]) # Negative Indexing : starts from end

wrd = "Ocygen"
new_wrd = wrd.replace('c', 'x') # replaces all occurrences of the provided character
print(new_wrd)

var = "String"
ans = var[2:6] # start:end - inclusive : exclusive
print(ans)

var = "String"
ans = var[0:5:2] # : step - skips after every character
print(ans)

s = "saffix"
idxm = 1
nch = 'u'
news = s[:1] + nch + s[2:] # to replace a part of string with new characters
print(news)

text = "Playground"
sim = text[::] # whole string from left to right
rev = text[::-1] # for traversing right to left
print(sim)
print(rev)

first, second = input().split()
fn = ord(first) # converts a character to its Integer code
sn = ord(second)
print(fn + sn)

num = int(input())
print(chr(num)) # converts integer to its Character