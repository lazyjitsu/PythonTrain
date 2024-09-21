import itertools

#counter = itertools.count()
counter = itertools.count(start=5,step=2)

# ann infiite loop; counts to infinity!!
# for num in counter:
#     print(num)

# or we can use next as it is an iterator
#print(counter)
# print(next(counter))
# print(next(counter))


# now suppose we wanted to pair two values together such as an index and a value
data = [100,200,300,400]
# zip tool combines two iterables and pairs their values together.

daily_data = zip(itertools.count(),data)
print(daily_data) #prints a zip object which is an iterable. we can conver to a list to print in one bang

daily_data = list(zip(itertools.count(),data))
print(daily_data)
# prints [(0, 100), (1, 200), (2, 300), (3, 400)]

#zip stops at the shortest size iterable. In this case, data is the shortest w/4 elements and range is set to 10 numbers so data[] dictaes when it stops
daily_data = list(zip(range(10),data))
print(daily_data)

daily_data = list(itertools.zip_longest(range(10),data))
print(daily_data)

## cycle will cycle through a list. it's an iterable

counter = itertools.cycle([1,2,3])
print(next(counter))
print(next(counter))
print(next(counter))

# another ecample using a tuple
counter = itertools.cycle(('On','Off'))

print(next(counter))
print(next(counter))
print(next(counter))

# repeat is simple and simply repeats 
counter = itertools.repeat(2,times=3)
print(next(counter))
print(next(counter))
print(next(counter)) #since it is set to only repeat twice, this line will print a stopIteration error. Use a for loop if u want to avoid that
# for looops handle the StopIteration exception for us...

# a practical example is using map
# this will use '2' as the power to raise the number, 1..10 from the range()
#i.e. 0^2,1^2,2^2...
squares = map(pow,range(10),itertools.repeat(2))
print(list(squares)) #lets avoid having to iterate through using a for loop and cast/print it as a list

# star map is like map but takes tuples as an argument

squares = itertools.starmap(pow,[(0,2),(1,2),(2,2)])

print(list(squares))

letters = ['a','b','c','d']
numbers = [0,1,2,3]
names = ['Corey','Nicole']

# recall combinations don't care about order. i.e. a,b is the same as b,a and thus will be listed just once. LIke a dec of cards u don't care if you have king and queen or queen and a king
# and show mme the commbinatins of two letters
results = itertools.combinations(letters,2)

for item in results:
    print(item)

# So if order does matter, we can use permutations. So note the list will be longer cause we want every order that is possible,hene we care about order!

results = itertools.combinations(letters,2)

for item in results:
    print(item)



# So with combinations we don't care about order so this means we don't do: a,b with b,a since we only care they appeared together not which one came first!
# permutations, we do care. e.g. a car race: we care which car came first and which second...order matters so we list every possible order
# now with products we care about oder but we don't care about repeats. This is great for like password breaking. Recall w/passwords its base^numberOfTimesWe do
# e.g. 27 letters in alphabet; if alpa only pass w/ 8 characters, we would have 27^8. So in the below we have 4(number of numbers in arrray) raised to 3 to give us 4^3=64

results = ''
results = itertools.product(numbers, repeat=3)
for item in results:
    print(item)

print(f"Len: {results.__sizeof__()}")
# u can also look at results = itertools.combinations_with_replacement(numbers, 3) which i performs like product.give it a test


## Lets look at chaining. What if we had 3 lists and wanted to iterate over all of them. We could do something like:

combined = letters + numbers + names

for i in combined:
    print(f"Eye: {i}")

# which is ok if your lists are short but if u have 10s of thousands or millions of elements, this would be naive.  or what if we had iterators not just lists. For this,
# we could use chains 

combined_again = itertools.chain(letters,numbers,names)

for item in combined_again:
    print(item)

# now islice is like slice where it can take slices or portions of a list but islice does it on iterattors.
# 
result = itertools.islice(range(10),5)
for i in result:
    print(i)
print('-----')
result = itertools.islice(range(10),1,5,2)  #start,stop,step
for i in result:
    print(i)

#so the below technique of grabbing just the first 3 header lines of a log file is far more preferable then loading a file that can be millions of lines long
with open('test.log','r') as f:
    headers = itertools.islice(f,3)
    for i in headers:
        print(f"Header: {i}",end='') # the file has a newline and print creates a newline. end will undef the newlines

# compress will take a allow you to use selectors on data and filter down that data. Let's say we have a list of True/False values that
# correspond to some data set 

letters = ['a','b','c','d']
numbers = [-2,-1,0,1,2,3]
names = ['Corey','Nicole']

selectors = [True,True,False,True]

result = itertools.compress(letters,selectors)

for item in result:
    print(item) # note this will NOT print 'c' since it corresopnds to 'False' in the selectors list

# now this looks a lot like filter except filter takes a function where compress takes a list or iterable

# here is an example of filter so we can compare

def lessThan2(n):
    if n < 2:
        return True
    return False

result = filter(lessThan2, numbers)

for i in result:
    print(i)

result = itertools.filterfalse(lessThan2, numbers)

#prints greater then 2 since it captures false values. 
for i in result:
    print(i)

numbers = [1,2,3,4]
result = itertools.accumulate(numbers)
print('*************')
for item in result:
    print(item)

import operator
print('*************')

result = itertools.accumulate(numbers,operator.mul)
for item in result:
    print(item)