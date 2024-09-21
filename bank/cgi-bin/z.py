import cgi
import cgitb
from typing import NamedTuple
import re

class mycolors:
    HEADER =     "\33[95m"
    Black =      "\u001b[30;1m"
    Red =        "\u001b[31;1m"
    Green =      "\u001b[32;1m"
    Yellow =     "\u001b[33;1m"
    Blue =       "\u001b[34;1m"
    Magenta =    "\u001b[35;1m"
    Cyan =       "\u001b[36;1m"
    White =      "\u001b[37;1m"
    Reset =      "\u001b[0m"

class Token(NamedTuple):
    type: str
    value: str

form = cgi.FieldStorage()
name=""
techmode=""
ops = {}10
opsidx = int(0)
def getDomain(d):
    #print(f"Called with {d}")
    for i in d:
        print(mycolors.Blue + f"Ops {i} ")
        for j in d[i]:
            for k in j:
                print(f"All: " + mycolors.Red + f" {j} " + mycolors.Blue + f"Root key " + mycolors.Red + f"{k} " + mycolors.Blue +  "and Root keys data " + mycolors.Red + f"{j[k]}")
    return k
data = [{'Domain':'Business Banking','DefAgent':'suzuiki123-mapped'},{'Domain':'Business Banking','DefAgent':'suzuiki124-mapped'},{'Domain':'Safeway','DefAgent':'wppi2345-app'},\
    {'Domain':'Safeway','DefAgent':'wppi2346-app'}]
def getAppID(s) :
    for i in range(len(data)):
        found = 0
        print(f"Searching for {data[i]['DefAgent']} EndSearch")
        if s == data[i]['DefAgent'] and found == 0:
            print(f"<h3 style=color:red;>Search completed...Found: {s} which belongs to domain: {data[i]['Domain']}</h3>")
            found = 1
        if len(ops) == 0:
            ops['Domain'] = [{data[i]['Domain']:{'DefAgent':[]}}]
            d = getDomain(ops)
            #print(f'First time here d: {d} length of ops {len(ops)} and length of data: {len(data)}')
            ops['Domain'][0][d]['DefAgent'].append(data[i]['DefAgent'])
            
            if data[i]['Domain'] == getDomain(ops):
                print(mycolors.Blue + f"!!!!The data {data[i]['Domain']} is same as ops domain: " + mycolors.Red + f"{getDomain(ops)}")
                ##Add agents and others to the same domain
            else:
                # we shouldn't be here because our length is zero!!
                print(mycolors.Blue + f"Diff!! data {data[i]['Domain']} is diff than  domain: " + mycolors.Red + f"{getDomain(ops)}")
        else:
            if len(ops) > 0:
                if  data[i]['Domain'] == getDomain(ops):          
                    print(f"!!!!The else data  "+ mycolors.Blue + f"{data[i]['Domain']} is same as ops domain: " + mycolors.Red + f"{getDomain(ops)}")
                    ops['Domain'][0][d]['DefAgent'].append(data[i]['DefAgent'])
            # this is the domain's data continued
            if data[i]['Domain'] == getDomain(ops):
                print(mycolors.Green + f"2nd record " + mycolors.Blue + f"{data[i]['Domain']} is same as ops domain: " + mycolors.Red + f"{getDomain(ops)}" )
                #ops['Domain'].append(data[i]['DefAgent'])
                print(mycolors.Yellow + f"---------------------------------------------------------------------------------------------------------------------------------------------------------")
                mycolors.White
            else:
                # the domain is now changed!! time to setup a new domain here if need be!!
                print(mycolors.Green + f"Data " + mycolors.Red + f"{data[i]['Domain']} " + mycolors.Green + "is NOT domain: " + mycolors.Red + f"{getDomain(ops)}")
                ops['Domain'].append({data[i]['Domain']:[data[i]['DefAgent']]})
                x = len(ops)
                print(mycolors.Green + f"Done with 2nd domain: {ops} andd {ops['Domain'][len(ops)].get(data[i]['Domain'])[0] } ")
            print(mycolors.Yellow + f"---------------------------------------------------------------------------------------------------------------------------------------------------------")
    return s

print("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<h1> App Page Boyyyz!</h1>")

def test(x):
    print(mycolors.Green+f"TEST: {x}")

#cgitb.enable(display=0, logdir="mycgilog.log")
def tokenize(agent):
    #print(f"<h2>Func received: {agent}</h2>")
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    agent_construction = [
        ('APACHE',           r'(?<=[a-z]{5}[0-9]{2}[a-z][0-9]{4})-([0-9a-z]{3,})'),  # Apache App aprrc12a1234-1abc
        ('APACHE2',          r'(?<=-)([0-9a-z]{3,})'),  # Apache App aprrc12a1234-1abc
        ('APPBEGIN',         r'[0-9]?[a-z]{3,4}(?=-unmappedhost$)'),           # App ID is at start  1edaz-unmappedhost
        ('IDFC',             r'[a-z]+(?=-idfcgateway)'),            # IDFC Gateway (Embedded WebAgent) whodat-idfcgateway
        ('APPWPORT',         r'([A-Za-z]{3})(?=-unmappedhost-[0-9]{4})'),    # App ID at end xft-unmappedhost-1234
        ('HOSTDASHAPPID',    r'([a-z]{4,7}[0-9]{4})-(\w+)'), #test cousin2000-mrcoolman
        ('CATCHALL',         r'(?<=[a-z]{2}\d[a-z]{4}[0-9]{3}-)\w+'),
    ]
    
    agent_expressions = '|'.join('(?P<%s>%s)' % instruction for instruction in agent_construction)
  
    for m in re.finditer(agent_expressions, agent):
        #print(mycolors.Green+f"\tReceived {agent} and Setting mode to {m.lastgroup} ")
        mode = m.lastgroup
        if mode == 'APACHE':
            value = m.group(2)
            print(f"\tApache {agent} detected with mode: {mode} and extracted: {value}")
            return print("<h2 style=color:red;>Application name: "+value+" with mode: " +mode+"</h2>")
        if mode == 'APACHE2':
            value = m.group(0)
            print(f"\tApache {agent} detected with mode: {mode} and extracted: {value}")
            return print("<h2 style=color:red;>Application name: "+value+" with mode: " +mode+"</h2>")
        if mode == 'APPWPORT':
            value = m.group(0)
            print(f'\tAPPWithPort {agent} detected with mode: {mode} and extracted: {value}')
            return print("<h2 style=color:red;>Application name: "+value+" with mode: " +mode+"</h2>")
        if mode == 'APPBEGIN':
            value = m.group(0)
            #print(f'\tAppBegin {agent} detected with mode: {mode} and extracted: {value}')
            return print("<h2 style=color:red;>Application namee: " +value+ "   with mode: " +mode+"</h2>")
            #return value
        if mode == 'IDFC':
            value = m.group(0)
            print(f'\tIDFC {agent} detected with mode: {mode} and extracted: {value}')
            return print("<h2 style=color:red;>Application name: " +value+ " with mode: " +mode+"</h2>")
        if mode == 'HOSTDASHAPPID':
            value = m.group(0).split('-')[1]
            print(f'HOSTDASHAPPID {agent} detected with mode: {mode} and extracted: {value}')
            return print("<h2 style=color:red;>Application name: " +value+ " with mode: " +mode+"</h2>")
        if mode == 'CATCHALL':
            value = m.group(0)
            print(f'CATCHALL {agent} detected with mode: {mode} and extracted: {value}')
            return print("<h2 style=color:red;>Application name: " +value+ " with mode: " +mode+ "</h2>")
        print(f"End : {mode} and {agent} and {value}")
        yield Token(mode, value)

if form.getvalue("name"):
    name = form.getvalue("name")
    print("<h1>You sent me: " +name+ " and so we shall now search for the participating system</h1><br />")
    if form.getvalue("prod"):
        print("<h3>You selected Production env for agent: "+name+"!</h3>")
       # print("<p style=color:blue;> We have detected  as the character sequence</p>")
        #print("<p style=color:blue;> We have detected  as the character sequence " + b + "</p>")
        #getAppID('salass boy')
        getAppID(name)
        for i in tokenize(name):
            continue
            

    if form.getvalue("uat"):
        print("<h3>You selected UAT bro!!</h3>")
    if form.getvalue("prodfix"):
        print("<h3>You selected ProdFix bro!!</h3>")
    if form.getvalue("sit"):
        print("<h3>You selected SIT!!</h3>")
    if form.getvalue("dev"):
        print("<h3>You selected Dev bro!!</h3>")
print("<p>You are finished with HTML page !!</p>")
print("</body></html>")

#print(f"Starting with {data}")
#print(f"<h2> OPS: {tokenize(ops['Domain'][0][d]['DefAgent'])}  </h2>")

#for agent in data:
 #   print("*********************************************")
  #  for token in tokenize('suzuki123-4444'):
   #     print(f"{type(tokenize('suzuki123-4444'))} and z.    Tttttttttttttttttoken Type: {token.type} and value: {token.value}")
        #print("Token Type: %-26s  Domain Substring: %s" %(token.type, token.value))

print(f" Done with ALL: {type(tokenize('wuszi1234'))}")