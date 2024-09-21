# Iterators vs. iterables.  Lists (arrays) are iterable but are NOT iterators. For an object to be iterable, it would need the dunder method, __iter__
# To see if an object has this method, use the dir method like so:

nums = [1,2,3]
print(dir(nums))
#['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', 
# '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', 
# '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#print(next(nums))
# will print
# Traceback (most recent call last):
#   File "D:\mySource\python\bank\headersTraining\loopsPractice.py", line 11, in <module>
#     print(next(nums))
# TypeError: 'list' object is not an iterator

# The reason we get an error is because this has no next method. The next() method is trying to run the dunder method, __iter__ in the background and can't find it.

# lets add it to numbs by renaming...and:
i_nums = nums.__iter__()  # now this adds the for loop stuff but u shouldn't run dunder methods directly
print(i_nums)
print(dir(i_nums))
# this i show to properly use dunder method

i_nums = iter(nums)

# now we have an iterator which is also iterable contrasted by an array which is not an iterator but is iterable! Now an iterator whichhas an iter dunder method 
# for iteration, simply returns 'self' and waits to be called via 'yield' which is my unnderstanding. Now we see the error above about not being an iterator and
# that's because there was no dunder __next__ method but usin gtthe iter() we now have one...
# so now we can do print(next(i_nums))
# Understand an iterator is an object with a state so that it remembers where it is during iteration
#  It loops until a StopIteration exception. It basically works like this:
# 
while True:
    try:
        item = next(i_nums)
        print(f"Item: {item}")
    except StopIteration:
        break

# so there is ONLY going foward. If you need to go back to the beginning, create another iterator. What is the practical
# point of know all this you ask? It's so that we can add these methods to our own classes and make them iterable as well!!
# Lets build a class that behaves like the range function

class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end
    
    # recall an iter method has to return an iterator. By that we mean the iter method has to return an object which has the dunder __next__ method
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

#  Now les use it

nums = MyRange(1,10)  #start at 1 and end at 10

for num in nums:
    print(num)
#iterator mode 

i_num = MyRange(1,5)
print(next(i_num))

## Now generators are functions that create iterators like our custom class, MyRange above and work the same but add the __next__ and __iter___ for us
# This isn't a class so we don't need self because we will not be working with instances
def my_range(start,end): 
    current = start
    while current < end:
        yield current
        current += 1

nums = my_range(1,5)
print(next(nums))
print(next(nums))

# Now an iterator doesn't have to end and can go forever might making the following modification. Basically an infinite loop!!
def my_range(start): 
    current = start
    while True:
        yield current
        current += 1

#nums_forever = my_range(1)

