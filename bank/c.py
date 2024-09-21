a = ["mike","marko","sam"]
b = ["marko","mike","sem","semster","girl"]

# for i in b:
#     if i in a:
#         print(f"Found {i}")
#     else:
#         print(f"CAn't find {i}")
import sys
file="list.txt"
a = []
# with open(file,'r') as fh:
#     for line in fh:
#         if len(a) == 0:
#             print(line.rstrip('\n'))
#             a.append(line.rstrip('\n'))
#         else:
#             if line.rstrip('\n') in a:
#                 continue
#             else:
#                 a.append(line.rstrip('\n'))
#                 continue
#     print(f"A: {a}")
#         #print(line.rstrip('\n'))

myDict = [{"one":1},{"two":2}]
myDict2 = [{"dose":2},{"one":1},{"two":2},{"tres":3},{"quatro":4}]
d = ["alex","one","two","tres","quatro","sem","freemont"]
not_found = []
next = ""
# for i in d:
#     found = False
#     # if next:
#     #     print(f"current has ((( {i} ))) and you've already been at the bottom")
        
#     for j in a:
#         print(f"\tComparing {i} and {j}")
#         if i in j.rstrip('\n'):
#             print(f"Found {i} in {j}")
#             found = True
#             break
#         else:
#             #print(f"\tCAn't find {i} in {j}")
#             continue
#     if found == False:
#         print('not found dude')
#         not_found.append(i)
#         found = False
#     print(f"Made it to the bottom with << {i} >> and current should come next")     
#     # next = True
# print(f"Elements of 'd' {d} were not_found: {not_found} in {a} ")
# import re
xpr=""
searchKey = sys.argv[1]
def getMe(t):
    xpr = ''
    print(f"Received: {t}x")
    if re.match('\s+$',t):
        print(f"Found space att teh end of: {t} !!")
        xpr = ".*" + t

    for i in churchData:
        for j in i:
            print(f"Checking expression {xpr} against: {j} ")
            if re.match(f'{t}$',j):
                print(f" Found {i[j]} with xpr: {xpr}    !!!!!!!")
import re
churchData = [{"bjj-it":"Rickson"},{"bjj-it":"Rockson"},{"bjj-itme":"Kron"},{"karate":"Henry"},{"kungfu":"IP Man"},{"kungfu":"WingChun"}]

def tokenizeSearchKey(s):
    if re.match('(\s+|-)[\w+]\s+',s):
        print(f"Mathced: {s} !!")
    print(f"Search: {s} !!")
getMe(searchKey)
#tokenizeSearchKey(sys.argv[1])