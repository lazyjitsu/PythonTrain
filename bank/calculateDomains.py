import re
#Domain: CMB-TestLocator
#Domain: GOT-CommonProfile
#Domain: WHL-NFTAIM
#Domain: WHL-ORACLEBIE
#Domain: CFI-OT2
domains = ['CMB-TestLocator','GOT-CommonProfile','WHL-NFTAIM','WHL-ORACLEBIE','CFI-OT2']
''' Goal: Create algorithm to determine domain/app id using the URL/FQDN
    Sceanrio 1: Org is in first position of description and Appid is in the 2nd position of description field in uppercase
    Scenario 2: Org is in first position and First word and First character of the following words up to 3 words
    Scenario 3: 

  ToDo: Look up 'Lending Central Data Repository' and see what domains, besides CFI-OT2, you can uncover to attempt to discern some pattern(s)  
''' 
name_can = []
data =[
       {'ACO':'aco-oraclebie-spprb99a3344','DefaultAgentName':'oraclebie-unmapped','Desc':'WHL,Oracle Business Intelligence Enterprise Edition,PRD,Apache,2.4','AgentName':
       'spprb99a3344-oraclebie,obiee-prod.coolbank.net\
        spprb99a3344-oraclebie,obiee.coolbank.net\
        spprb99a3344-oraclebie,spprb99a3344.coolbank.net\
       ' },
       {'ACO':'aco-ot2-idfc','DefaultAgentName':'ot2-unmapped','Desc':'Lending Central Data Repository, IDFC PROD','AgentName':
       'ot2-idfcgateway,ot2.ls03ad2.azure.coolbank.net:443\
        ot2-idfcgateway,ot2.ew03ad2.azure.coolbank.net:443\
        ot2-idfcgateway, ot2.ew03ad2.azure.coolbank.net \
       '},
       {'ACO':'aco-commonprofile-wuszi97a185-9002','DefaultAgentName':'Commmonprofile-unmappedhost','Desc':'GOT, CPA,Prd','AgentName':
       'cpa-idfcgateway,cpadmin.ox9ab3.azure.coolbank.net:443\
        cpa-idfcgateway,cpadmin.vs04ab3.azure.coolbank.net:443\
        cpa-idfcgateway,cpadmin.coolbank.net:443 \
        cpa-idfcgateway,querytool.ox9ab3.azure.coolbank.net:443 \
        cpa-idfcgateway,querytool.vs04ab3.azure.coolbank.net:443\
        cpa-idfcgateway,querytool.coolbank.net:443'
        },
        {'ACO':'aco-TestLocator-wrca233b0000','DefaultAgentName':'TestLocator-unmappedhost','Desc':'CMB,TestLocator,Prod,IIS,8','AgentName':
       'abcde00a0012-testLocator,abcde00a0012.wellsfargo.com:443\
        abcde00a0012-testLocator,testLocator.wellsfargo.com'
       },
       {'ACO':'aco-b2web-idfc','DefaultAgentName':'b2web-unmappedhost','Desc':'WHL, NFTAIM,CloudFoundry,Prod','AgentName':
        'b2web-idfcgateway,aim.fcapps.coolbank.net\
        b2web-idfcgateway,ac1234-b2web-prodox.apps.oxdcarh-p-11-fc-coolbank.net:443\
        b2web-idfcgateway,ac1234-b2web-prodvs.apps.vsdcarh-p-11-fc-coolbank.net:443'
       },
     ]

# test ^ with beginning of line vs. beginning of string and does '$' come before or after newline..retest
appAcronym = ""
desc_sizes = []
for i in data:
    aco = i['ACO']
    #desc = i['Desc'].split(',')[1].replace(' ','')
    desc = i['Desc'].split(',')[1]
    agents = i['AgentName']
    defAgentName = i['DefaultAgentName'].split('-')[0]
    print(f"Def: {defAgentName}")
    for d in domains:
        if re.match(f'.*-{defAgentName}',d,re.IGNORECASE):
            print(f"\tFoundd: {defAgentName} in {d}")
   # print(f"Checking {desc} ")
    #Special case
    if re.match(r'(\w+\s+)+\s?',desc):
        print(f"Found desc: {desc} {i['DefaultAgentName'].split('-')[0]}")
        for j in re.findall('([A-Z])+',desc):
           appAcronym += j.lower()
        name_can.append(i['DefaultAgentName'].split('-')[0])



for i in name_can:
    desc_sizes.append(len(desc))
    #print(desc_sizes.sort())
name_can.append(appAcronym)
print(appAcronym)
desc_sizes.sort()
print(desc_sizes)
print(name_can)

for n in name_can:
    print(f"Checking N: {n}")
    for d in domains:
        #print(f"N:{n} D: {d}")
        if re.match(rf'.*-{n}',d,re.IGNORECASE):
            print(f"Matched :{n} to {d}")


    
print('------------------------------------------')
d = ['WHC-Marko','WHC-Marko','CMB-CashMoney','STW-StrawMan','STW-StrawMan']

#print(d)
tmp = ""
l = []
for i in d:
    print(f"t: {tmp} and i: {i}")
    if tmp != i:
        l.append(i)
        tmp = i
    else:
        print(f"Same: {tmp} and {i}")
print(f"Done {l}")


dum = ['pytho']

print('*******************************')
for i in dum:
    if re.search('(?!<unmapped)-.*$',i):
        print(i)

#print(dum)