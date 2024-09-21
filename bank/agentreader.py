import glob
import sys
#print('\nNamed with wildcard *:') 
class mycolors:
    HEADER = "\33[95m"
    Black = "\u001b[30;1m"
    Red =  "\u001b[31;1m"
    Green = "\u001b[32;1m"
    Yellow = "\u001b[33;1m"
    Blue = "\u001b[34;1m"
    Magenta = "\u001b[35;1m"
    Cyan = "\u001b[36;1m"
    White = "\u001b[37;1m"
    Reset = "\u001b[0m"
wellsdata = {}
for name in glob.glob(r'D:\mySource\python\bank\server*'):
    #name.split("\\")[-1] + '_data' = []
    #print(name.split("\\")[-1] + '_data')
    print(sys.argv[0])
    if name.split("\\")[-1] == sys.argv[0]:
        print('Found program: ', sys.argv[0])
    else:
        file = name + '\webagent_log.txt'
        server_name = name.split("\\")[-1]
        data_file = server_name + '-webagent.log'

        wellsdata = { server_name:{ 'log file': { data_file: [] } } }
        print('opening: ' + name)
        current_file = open(file,'r')
        data = current_file.readlines()        
        current_file.close()
        print(data)
        # mylist = [1,2,3,4,5,6]
        ''' a = mylist[::2] print every other element. great for color coding lines '''
print(wellsdata)

