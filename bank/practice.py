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
    appID: str

#'abc-unmappeshost-1234','unmappedhost-ghi-4321',
a = ['mikeo14s9876-usa','def456-99','ps4mzmt239-abccz','wpvra14a2391-si','wpvra14a2391-unmappedhost','larvr00b1234-mti','brbi-unmappedhost','arvve88a0014-sweat','sp3mzmt333-bapps','marko-14','sss123-11','abc123-aa','xxx379-82']
u='unmappedhost'
def tokenize(code):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
#       ("TEST",             rf"[a-z]{5}[0-9]{2}[a-z][0-9]{4}-{{u}}")
       #("TEST",       ("TEST",             rf"[a-z]{5}[0-9]{2}[a-z][0-9]{4}-(?!{u})(\w+)")
        ("TESTNOMAP",           rf"[a-z]{{5}}[0-9]{{2}}[a-z][0-9]{{4}}-(?!{u})(?![0-9]{{2}})(\S+)"),
        ("TESTMAP",             rf"\w+-(?={u})({u})"),
        ("PREHYPH",             rf"(\w+)(?=-[0-9]{{2}})"),
        ("CRAZYHOST",           rf"(?:[a-z]{{2}}[0-9][a-z]{{4}}[0-9]{{3}})-(?!{u})(?![0-9]{{2}})(\S+)"),
        ("PREHYPHALPHA",        rf"(\w+)(?=-[a-z]{{2}})"),

    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    # for pair in token_specification:
    #      print(pair)
  
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        #value = mo.group(2)
        if kind == 'TESTNOMAP':
            appID = mo.group(2) + '   :TESTNOMAP'
        if kind == 'TESTMAP':
            #appID = mo.group(4) + ':TESTMAP'
            appID = mo.group(4) + '   :TESTMAP'
        if kind == 'PREHYPH':
          
            appID = mo.group() + '   :PREHYPHDIGI'
        if kind == 'CRAZYHOST':          
            appID = mo.group(8) + '   :CRAZYHOST'
           # print(f"Kind: {kind} and value: {value} and col: {column}")
        if kind == 'PREHYPHALPHA':          
            appID = mo.group(10) + '   :PREHYPHALPHA'
           # print(f"Kind: {kind} and value: {value} and col: {column}")
        
        elif kind == 'MISMATCH':
            raise RuntimeError(mycolors.OKBLUE + f'{appID!r} unexpected on line {line_num}')
        yield Token(kind, appID)

count = int(0)
for agent in a:
    for agent_token in tokenize(agent):
        count += 1
        if re.search(f'(?=^{u})',agent_token.appID):
            print(f"\t\tAgent with no app data token val: {agent_token.appID}")
        else:
            print(mycolors.Blue + f"Found application: << " + mycolors.Green + f"{agent_token.appID} " + mycolors.Blue + ">> !!")


print(f"Length: {len(a)} and agents: {count}")