import re

t = ['abc','north']


import wellsSMLib as wl


for i in t:
    print(f"Sending {i}")
    #print(wellsSMLib.printMe())
    wl.getDomain(i)



