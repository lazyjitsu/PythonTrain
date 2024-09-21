import re

domains = []
with open('domains.txt','r') as f:
    lines = f.readlines()
    for i in lines:
        #print(f"Eye: {i}",end='')
        domains.append(i)
with open('agents.txt','r') as f:
    agents = f.readlines()
    for a in agents:
        ptn = a.rstrip().upper()
        for d in domains:
            #print(f"Checking {ptn} and {d}",end='')
            if re.match(f"[A-Z]{{3}}-{ptn}",d):
                print(f"\tFound: {d.rstrip()} with {ptn}")
            else:    
                continue
