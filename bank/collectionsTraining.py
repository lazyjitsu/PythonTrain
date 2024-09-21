from collections import Counter
#collections: Counter, namedTuple, OrderedDict, defaultdict,deque
# Counter
mystr="aaaaabbbbbccc"

mycol = Counter(mystr)
print(mycol)
print(mycol.keys())
print(mycol.values())
print(mycol.most_common(1))
from collections import namedtuple

# namedTuple
# the left Point must match the same name in namedTuple arg of 'Point'
Point = namedtuple('Point', 'x,y')
pt = Point(1,-3)
print(pt)

print(pt.x,pt.y)
# OrderedDict
from collections import OrderedDict
# with 3.7 or higher, normal dicts remember too
ordered_dict = OrderedDict()

ordered_dict['a']  = 1
ordered_dict['b']  = 2
ordered_dict['c']  = 3
ordered_dict['d']  = 4
# remembers the order in which they were inserted.
print(ordered_dict)
mydict = {}

mydict['a']  = 1
mydict['b']  = 2
mydict['c']  = 3
mydict['d']  = 4

print(mydict)

# defaultdict. same as a regular dict except a default value is provided for key if one isn't assigned
from collections import defaultdict
# defaultdict(int), defaultdict(float), defaultdict(list)
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['c']) #will default to 0

# deque

from collections import deque

d = deque()
d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
d.extend([1,3,4])
print(d)
d.extendleft([6,7,8])
d.rotate(1)
d.rotate(2)

# rotate on left side
d.rotate(-1)

# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

# product (calculates the cartesian product)
# 
from itertools import product
a = [1,2]
b = [3,4]

prod = product(a,b)
print(prod)
print(list(prod))
a = [1,2]
b = [3]

prod = product(a,b, repeat=2)
print(list(prod))

# calculate the number of ways we can order a list 
from itertools import permutations
a = [1,2,3]
perm = permutations(a)
print(list(perm))
# length of 2
perm = permutations(a,2)
print(list(perm))

from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a,2) # length 2 and length is required for this fcn

print(list(comb))
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))

from itertools import accumulate

a = [1,2,3,4]
acc = accumulate(a)

print(a)
print(list(acc))
import operator

acc = accumulate(a, func=operator.mul) #multiply

print(a)
print(list(acc))
a = [1,2,5,3,4]

acc = accumulate(a, func=max)

print(a)
print(list(acc))

from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1,2,3,4]

group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

    
