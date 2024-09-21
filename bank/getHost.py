import os
import sys
import subprocess

my_list = open(sys.argv[1])
for i in my_list:
    print(i.strip())
    list_hosts = subprocess.run(["cmd","ssh",i])

#list_files = subprocess.run(["ssh",])
#print(list_files.returncode)