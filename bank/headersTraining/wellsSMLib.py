import re
d = ['DMZ-NORTH','DMZ-NORTH','ABC-DEF']
matched = []
def getDomain(t):
        ptn = t.rstrip()
        for domain in d:
            if re.match(f'[a-z]{{3}}-{ptn}',domain,re.I):
                print(f"Matched {domain} with {t}")
                matched.append(d)
        return matched

def printMe():
    return "puro Salas"