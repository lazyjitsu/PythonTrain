
import csv
import json
import re

class mycolors:
    HEADER =     "\33[95m"
    Black =      "\u001b[30;1m"
    Red =        "\u001b[31;1m"
    Green =      "\u001b[32;1m"
    Yellow =     "\u001b[33;1m"
    Blue =       "\u001b[34;1m"
    Magenta =    "\u001b[35;1m"
    Cyan = "\u001b[36;1m"
    White = "\u001b[37;1m"
    Reset = "\u001b[0m"


data = {}
data["world2k"] = []

policies = []
domain_cnt = int(0)
policy_cnt = int(0)
store_cnt = int(0)
resource_cnt = int(0)
current_dom = ''
current_rsc = ''
current_store = ''
current_pol = ''

# data = { "world2k" : [
#                     {'WhlSale':
#                         [
#                             {'Policy1':
#                                 [ 
#                                     {'Realm1':[    
realms = []

with open('realms.csv') as csvfile:
    realm_reader = csv.DictReader(csvfile)
    for realm in realm_reader:
        realms.append(realm)

print(realms)
with open("policy.csv") as csvfile:
    policy_reader = csv.DictReader(csvfile)
    for policy in policy_reader:
        if current_dom: # we have the strucutre initialized and now reading 2nd line
            print(mycolors.Blue + f"post init: (( " + mycolors.Red + f"{current_dom,current_pol} " + mycolors.Blue + "))")
            #current_dom = policy['Domain']
            if current_dom == policy['Domain']:
           
                print(f"\tDomain equal block: { current_dom,policy['Domain']}")
                #print(f"Entered ((if)) Current Resource: (({ current_dom,current_pol,current_store,current_rsc } ))")
                if current_pol == policy['Policy']:
                    print("\t\t--**--**Entered policy condition")
                    #if current_rsc != data['world2k'][domain_cnt]['WHL-SEM'][policy_cnt][' Sem Policy'][store_cnt][policy['User Store']][resource_cnt] :
                    if current_store == policy['User Store']:
                        #print('\t\t\t\tEntered store condition')
                        print(f"Resource PUSH: {data['world2k'][domain_cnt],current_dom}")

                    else:
                        print('did not mmatch user store')
                else:
                    data['world2k'][domain_cnt][current_dom].append({policy['Policy']:[{'Agent Group':'',policy['User Store']:[policy['Resource']] }] })
                    print(mycolors.Green + f": Policy Differential {current_pol,policy['Policy']} " )
            else:
                print(f'domains not equalll: {current_dom,policy["Domain"]}')
                data['world2k'].append( { policy['Domain']:[{policy['Policy']:[{'Agent Group':'',policy['User Store']:[policy['Resource']] }] }] })
                current_dom = policy['Domain']
                current_pol = policy['Policy']
                current_store = policy['User Store']
                current_rsc = policy['Resource']
                domain_cnt += 1
                continue
        else:
            print("***********Starting a new domain!!*********************")  # should only be ran once!!
            data['world2k'].append( { policy['Domain']:[{policy['Policy']:[{'Agent Group':'',policy['User Store']:[policy['Resource']] }] }] })
            current_dom = policy['Domain']
            current_pol = policy['Policy']
            current_store = policy['User Store']
            current_rsc = policy['Resource']
            continue
print('-------------------------------')

# "world2k": [
#     {
#       "WHL-SEM": [
#         {
#           " Sem Policy": [
#             {
#               "Agent Group": "",
#               " Sem store": [
#                 " /sem"
#               ]
#             }
#           ],
for root_idx in range(0,len(data['world2k'])):
    for domain_name in data['world2k'][root_idx]:
        for domain_idx in range(0,len(data['world2k'][root_idx][domain_name])):
            for policy_name in data['world2k'][root_idx][domain_name][domain_idx]:
                print(f"RootIdx: {root_idx,domain_name,data['world2k'][root_idx][domain_name][domain_idx],policy_name}")
                for agent_grp_idx in range(0,len(data['world2k'][root_idx][domain_name][domain_idx][policy_name])):
                    print(f"A: {data['world2k'][root_idx][domain_name][domain_idx][policy_name][agent_grp_idx]['Agent Group']}")
                    data['world2k'][root_idx][domain_name][domain_idx][policy_name][agent_grp_idx]['Agent Group'] = "Salas:" + domain_name
#     for j in range(0,len(realms)):
#         for domain_name in data['world2k'][root_idx]: # get domans out  of the env index
#             for domain_idx in range(0,len(data['world2k'][root_idx][domain_name])):
#                 print(f"DomainIDX: {data['world2k'][domain_idx][domain_name]}")
                # for policy_name in data['world2k'][root_idx][domain_name][domain_idx]:
                #     for policy_idx in range(0,len(data['world2k'][root_idx][domain_name][domain_idx][policy_name])):  
                #         print(f"PP: {policy_name,policy_idx}")
                #         if domain_name == realms[j]['Domain']:
                #             print(f"K: {root_idx,domain_name,domain_idx,data['world2k'][root_idx][domain_name][domain_idx]}")
            #print(f"\tNOW: {data['world2k'][i][k][(len(data['world2k'][i][k]) - 1)]}")

# for i in realms:
#     print(f"RealmI: {i['Domain'],i['Agent Group']}")

def item_generator(json_input, lookup_key):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)

for i in realms:
    #print(f"RealmI: {i['Domain']}")
    #print(item_generator(data['world2k'],i['Domain']))
    for i in item_generator(data['world2k'],i['Domain']):
        print(f"Generator: {i}")
print(json.dumps(data,indent=2))

