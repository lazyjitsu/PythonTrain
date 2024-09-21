import re
import csv
import json
a = [{"Domain":"WHL-SEM"},{"Domain":"ABC-1LOVE"},{"Domain":"ABC-1LOVE"},{"Domain":"BCD-MAKEME"},{"Domain":"CDF-WHAT"}]

found = []
domain_data = {}

domain_data ["world2k"] = []


with open('policy.csv') as csvfile:
    csv = csv.DictReader(csvfile)
    for i in csv:
        domain_data["world2k"].append({i['Domain']:[i['Policy']]})        
        print(f"TU: { type(domain_data['world2k'][0] ) } ")

        #domain_data['world2k'][i['Domain']].append(i['Policy'])
        print(f"Type: { domain_data['world2k'] }")

        #print(f"Eye:{i}")


def getMe(key):
    found = ""
    for i in a:
        if re.match(f'.*{key}',i['Domain'],re.I):
            found = True
            print(f"Checking {i}")
            if found:

                print(f"Key found: {key} and {i['Domain']}")
            else:                
                break
        else:
            found = False

b = ["1LOVE"]

# for key in b:
#     getMe(key)


print(f"Done:{domain_data}")
for d in domain_data:
    print(f"Root:{d} and {domain_data[d]}")
    for e in range(0,len(domain_data[d])):
        #print(f"More: {domain_data[d][e]}")
        for f in domain_data[d][e]:
            print(f"Agan: {domain_data[d][e][f]}")


Dict = {'Dict1': {'name': 'Ali', 'age': 19},
        'Dict2': {'name': 'Bob', 'age': 21}}

for d in Dict:        
    print(Dict[d]['name'])


    #for e in Dict[d]:
