import csv
import json
import re
# data = { "world2k" : [
#                     {'WhlSale':
#                         [
#                             {'Policy1':
#                                 [ 
#                                     {'Realm1':[                                        
#                                         {'Desc':'mu Realm 1 and Policy 1 stuff',
#                                         'Agents':['a1','a2'] 
#                                         }       
    
#                                             ]
#                                     },
#                                     {"Realm2": [



data = {}
data["world2k"] = []

policies = []
cnt = int(0)
with open("policy.csv") as csvfile:
    policy_reader = csv.DictReader(csvfile)
    for policy in policy_reader:
       # print(f"t: {policy}")
        if data['world2k']:
            data['world2k'].append({policy['Domain']:[{policy['Policy']:[{policy['User Store']:[policy['Resource']]}]}]})

            print(f"if: {data} and len: {len(data)} and {len(data['world2k'])}")
            #print(f"Domain from file: {policy['Domain']} domain from struct: and Policy {policy['Policy']}")
        else:
            print(f"else: {data}")
            #print(f"else Domain from file: {policy['Domain']} domain from struct: {data['world2k'][cnt]} Policy {policy['Policy']}")
       # print(f"\tLength: {len(data['world2k']),cnt} count test: {data['world2k'][cnt][policy['Domain']]}")

        #data['world2k'].append({policy['Domain']})

            data['world2k'].append({policy['Domain']:[{policy['Policy']:[{policy['User Store']:[policy['Resource']]}]}]})
        #     if x in policy['Domain']:
        #         data['world2k'][cnt][policy['Domain']].append(policy['Policy'])
        #         print(f"x,y: {x,y}")
        cnt += 1

        #print(f"Testt: {cnt,data['world2k'][cnt].keys(),data['world2k'][cnt][policy['Domain']]}")

        #data['world2k'][policy['Domain']] = []


        #any(policy['Domain'] in d for d in data['world2k'])    

print("-------------------------------------------")
#json_converted_data = json.dumps(data,indent=3)

#print(f"Data: {json_converted_data}")
print(f"Data: {json.dumps(data,indent=2)}")