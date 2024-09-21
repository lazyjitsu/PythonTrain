from typing import NamedTuple
import re

class Token(NamedTuple):
    type: str
    value: str

#a = ['brbi-unmappedhost','arvve88a0014-sweat','sp3mzmt333-bapps','rrvrb00z0006-fusion','axvww00z0304-1bop','mnfmnf-idfcgateway','aprrc12a1234-1abc','1baas-unmappedhost','xft-unmappedhost-1234','1edaz-unmappedhost','abcdefgh001-zzmidtier','cousin2000-mrcoolman','whodat-idfcgateway','semon14a8888-speedtrack']
a = ['brbi-unmappedhost','arvve88a0014-sweat','sp3mzmt333-bapps']
#Don’t wish it was easier, wish you were better. Don’t wish for less problems, wish for more skills. Don’t wish wish for less challenges, wish for more wisdom. -Jim R. 
def tokenize(agent):
    print(f"Func received: {agent}")
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    agent_construction = [
        ('APACHE',           r'(?<=[a-z]{5}[0-9]{2}[a-z][0-9]{4})-([0-9a-z]{3,})'),  # Apache App aprrc12a1234-1abc
        #('APACHE',           r'-([0-9a-z]{3,})'),  # Apache App aprrc12a1234-1abc
        ('APPBEGIN',         r'[0-9]?[a-z]{3,4}(?=-unmappedhost$)'),           # App ID is at start  1edaz-unmappedhost
        ('IDFC',             r'[a-z]+(?=-idfcgateway)'),            # IDFC Gateway (Embedded WebAgent) whodat-idfcgateway
        ('APPWPORT',         r'([A-Za-z]{3})(?=-unmappedhost-[0-9]{4})'),    # App ID at end xft-unmappedhost-1234
        ('HOSTDASHAPPID',    r'([a-z]{4,7}[0-9]{4})-(\w+)'), #test cousin2000-mrcoolman
        ('CATCHALL',         r'(?<=[a-z]{2}\d[a-z]{4}[0-9]{3}-)\w+'),
    ]
    
    agent_expressions = '|'.join('(?P<%s>%s)' % instruction for instruction in agent_construction)

    for m in re.finditer(agent_expressions, agent):
        print(f"\tReceived {agent} and Setting mode to {m.lastgroup} ")
        mode = m.lastgroup
        if mode == 'APACHE':
            value = m.group(2)
            print(f"\tApache {agent} detected with mode: {mode} and extracted: {value}")
        if mode == 'APPWPORT':
            value = m.group(0)
            print(f'\tAPPWithPort {agent} detected with mode: {mode} and extracted: {value}')

        if mode == 'APPBEGIN':
            value = m.group(0)
            print(f'\tAppBegin {agent} detected with mode: {mode} and extracted: {value}')
            #agent = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
        if mode == 'IDFC':
            value = m.group(0)
            print(f'\tIDFC {agent} detected with mode: {mode} and extracted: {value}')
        if mode == 'HOSTDASHAPPID':
            value = m.group(0).split('-')[1]
            print(f'HOSTDASHAPPID {agent} detected with mode: {mode} and extracted: {value}')
        if mode == 'CATCHALL':
            value = m.group(0)
            print(f'CATCHALL {agent} detected with mode: {mode} and extracted: {value}')

        print(f"End : {mode} and {agent} and {value}")
        yield Token(mode, value)

for agent in a:
    for token in tokenize(agent):
        #print(f"Token Type: {token.type} and Domain/App ID: ---------------> {token.value}")
        print("Token Type: %-26s  Domain Substring: %s" %(token.type, token.value))
