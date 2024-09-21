courses = ['History','Math','Physics','CompSci']

print(courses[-1]) # prints last element of array!. this is easier when u don't wantt to deal w/the length. I like it!
print(courses[0:2]) # print elements 0 and 1; 2 is not inclusive
print(courses[0:2]) # same thing. the 0 is implied in this context

print(courses[2:]) # print index 2 and go all the way to the end!



# add art to the  end
courses.append('art')

# now add Science to a specic location, index 0 in this case
courses.insert(0,'Science')

print(courses)
# now if u wanted to insert a couple courses in the beginning of the array
courses_2 = ['Cooking,','Education']
#courses.insert(0, courses_2) # will create a new array inside the original array!! we may not want that
# .append() will do the same as insert and give u that extra array. if u just wannted the values, use extends
courses.extend(courses_2)
print(courses)

# to remove a specific item
courses.remove('art')
# to remove at the end, simply use pop
courses.pop()  # pop() returns the item removed so u can get that by doing: popped = courses.pop()

# to sort, simply use sort (default is ascending)
courses.sort()
# to order in descendng use
courses.sort(reverse=True)

#.sort() will change the array because it sorts in-line. To not affect the original array, use sorted()

original_arr = sorted(courses)  # save off the original cause it will be changed!

# min,max,sum are simply sum(courses),min(sum) etc..

# to find the index of a value
courses.index('Math')
# to get a true or false instead of index:
print('Math' in courses)

# To get index and value
for index, course in enumerate(courses):
    print(index,course)

# we can also control where we start

for index, course in enumerate(courses,start=1): # not i think it starts the count not the actual element in the array!
    print(index,course)

# To create a string out of an array:
course_string = '-'.join(courses)  # will create on string w/hyphen in between
# to get back the origina array,
backToOrig  = course_string.split('-')

## Tuples are just like lists except they are immutable which means u can't change them

tuple_1 = ('History','Math','Physics')
tuple_2 = tuple_1

print(tuple_1)

## Sets are unordered and have no duplicates. they're good at testing for membership

cs_courses = {'History','Math','Physics','CompSci','Math'}
print(cs_courses) # will print 'Math' only once

print('Math' in cs_courses)

cs_courses = {'History','Math','Physics','CompSci'}
art_courses = {'History','Math','Art','Design'}

print(cs_courses.intersection(art_courses))
# the above tells u what courses in art are in cs but to find out what is NOT in
print(cs_courses.difference(art_courses))
# to get all courses from both sets w/out, of course, print duplicaes...use:
print(cs_courses.union(art_courses))




