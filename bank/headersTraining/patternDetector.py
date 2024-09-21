import sys
import re
agent_counts = {}
agent_names = ['aa','aabb1','11aabb','abc-123']
cnt = int(0)


def countPattern(s):
    alpha = int(0)
    digits = int(0)
    hyphens = int(0)
    pattern = ''
    frequency_counter = {}
    alpha_name = ''
    digit_name = ''
    #11aabb22a
    name_ptn = []
    for char in s:
        if re.match('[a-z]',char):
            #print(f'Character found: (( {char} ))')
            alpha += 1
            if digits > 0:
                #print(f"\tDigit Count: {digits}")
                name_ptn.append(str(digits) + 'digits')
                digit_name = str(digits) + 'digits'
                digits = 0
        #print(f'between matching ALPHA: {alpha} and DIGITS: {digits}')
        if re.match('[0-9]',char):
            #print(f'Character found: (( {char} ))')
            digits += 1
            if alpha > 0:
                alpha_name = 'alpha' + str(alpha)
                #print(f"\tAlpha count: {alpha}")
                digit_name =  str(digits) + 'digit'
                name_ptn.append(str(alpha) + 'alpha')
                alpha = 0
        if re.match('[-]',char):
            hyphens += 1
            print(f"Hyp count: {hyphens}")
                
        if re.match('[^a-z0-9]',char):
            hyphen_name = str(hyphens) + 'hyphens'
            name_ptn.append(hyphen_name)

        # print('bottom of IFs')
    #name_ptn.append(alpha)
    if digits:
        name_ptn.append(str(digits) + 'digit')
    elif alpha:
        name_ptn.append(str(alpha) + 'alpha')        
    #print(f"End Alpha : {alpha} and digits: {digits}")

    # print('-------------')
    # print(name_ptn)
    final_name = ''.join(name_ptn)
    # print(f"Final: {final_name}")
    return final_name

#countPattern(sys.argv[1])

    #print(countPattern(i))
    #print(f"Eye: {countPattern(i)}")
#print(agent_counts)

def p(x):
    return x + ':mikeo'

for i in agent_names:
    print(f"Agent name: {i}  and Pattern Name: {countPattern(i)}")

print('****************************++++++++++++++*')
# print(countPattern('aa'))
# print(countPattern('aabb11'))
