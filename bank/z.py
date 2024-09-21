from typing import NamedTuple
import re
import sys
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

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")


a = ['mikeo14s9876-usa','def456-99','ps4mzmt239-abccz','wpvra14a2391-si','larvr00b1234-mti','brbi-unmappedhost','arvve88a0014-sweat','sp3mzmt333-bapps','marko-14','abc123-11','abc123-aa','xxx379-82']
#Don’t wish it was easier, wish you were better. Don’t wish for less problems, wish for more skills. Don’t wish wish for less challenges, wish for more wisdom. -Jim R. 
def tokenize(agent):
    print(mycolors.Green + f"Begin tokenization for: {agent}")
    agent_construction = [
        ('APACHE',           r'(?=[a-z]{5}[0-9]{2}[a-z][0-9]{4}-[a-z]{2})(?:[a-z]{5}[0-9]{2}[a-z][0-9]{4}-)([a-z]{2,})'),  # Apache App aprrc12a1234-1abc
        ('APPEND',           r'(?=[a-z]{2}[0-9][a-z]{4}[0-9]{3}-[a-z]{5})(?:[a-z]{2}[0-9][a-z]{4}[0-9]{3}-)([a-z]{5})'),
        ('SEM',              r'(?=marko-14)(?:marko-)(14)',),
        ('SEM2',             r'(?=abc123-11)(?:[a-z]{3}[0-9]{3}-)(\d+)',),
        ('SEM3',             r'(?=[a-z]{3}[0-9]{3}-\d\d)(?:[a-z]{3}[0-9]{3}-)(\w+)'),


        #('APPEND',           r'(?=sp3mzmt333-bapps)(?:sp3mzmt333)(-bapps)')
    ]
    
    agent_expressions = '|'.join('(?P<%s>%s)' % instruction for instruction in agent_construction)

    for m in re.finditer(agent_expressions, agent):
        if m:
            print(f"Starting: {m}")
            #print(mycolors.Magenta + f"\tReceived " + mycolors.Yellow + f"{agent} " + mycolors.Magenta + f"and Setting mode to " + mycolors.Yellow +f"{m.lastgroup} ")
            print(mycolors.Red + f"Last group: {m.lastgroup}")
            mode = m.lastgroup
            if mode == 'APACHE':
                value = m.group(2)
                print(mycolors.Magenta + f"\tApache agent " + mycolors.Yellow + f"{agent} " + mycolors.Magenta + mycolors.Magenta + f"and extracted: " + mycolors.Yellow +f"{value}")
                print(f"apache groups: {m.groups()}")
                

            if mode == 'APPEND':
                length = len(m.groups())
                value = m.group(4)
                print(f"APPEND: {m.groups()} and value: {value}")


            if mode == 'SEM':
                value = m.group(6)
                print(f'\tAPPEND {agent} detected with mode: {m.groups()} and extracted: {value} allgroups: {len(m.groups())}')
                #agent = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
                #if value:

            if mode == 'SEM2':
                value = m.group(8)
                print(f'SEM2 {agent} detected with mode: {m.groups()} and extracted: {value} allgroups: {len(m.groups())}')
                #agent = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
                #if value:

            if mode == 'SEM3':
                value = m.group(10)
                print(f'SEM2 {agent} detected with mode: {m.groups()} and extracted: {value} allgroups: {len(m.groups())}')
                #agent = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
                #if value:
        yield Token(mode, value)
        # break
        #print(mycolors.Green + f"End : {mode} and {agent} and {value}")


for agent in a:
    for token in tokenize(agent):
        #print(f"Token Type: {token.type} and Domain/App ID: ---------------> {token.value}")
        print(mycolors.Blue + f"Token Type: " + mycolors.Red +f"{token.type} " + mycolors.Blue + f"Significant String: " + mycolors.Red + f"{token.value}")
