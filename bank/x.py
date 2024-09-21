import re

#a = ["ffcde00x0004-xiv","abxxi33a0014-p3c","sexrbuei3299-absak"]
a = ["1abc-unmappedhost","1abc-2ab-unmappedhost","salis-idfcauthportal","idfcgatewaydefaultv99-unmappedhost","denyrootidfc-sac","abcde12a1234-unmappedhost","tcx-unmappedhost-1234","tvboyz-unmappedhost","tcx-unmappedhost-1234","apvrr32x0044-unmappedhost","spam-unmappedhost","1tvboyz-unmappedhost","1sade-unmappedhost","liceduhs-unmappedhost","ufos-unmappedhost","servicingautodepartment-unmappedhost"]
'''
salis-idfcauthportal
idfcgatewaydefaultv99-unmappedhost
denyrootidfc-sac
'''
u = re.compile("[a-z]{8}[0-9]{4}|[a-z]{5}[0-9]{2}[a-z][0-9]{4}-unmappedhost")


for i in a:
     #u="unmappedhost"
     #print(u)
     print(u.search(i))
     #print(f"Checking {i}")
     #it = re.finditer(f'(?=^[a-z]{3}-{u})([a-z]{3})',i)it = 
     #it = re.finditer(f'(?=[a-z]{{3}}-{u})(^[a-z]{{3}})-{u}|(?=[a-z]{{4}}-{u})(^[a-z]{{4}})',i)
     #it = re.finditer('(?:([a-z]{8}[0-9]{4}|[a-z]{5}[0-9]{2}[a-z][0-9]{4})|([a-z]{3,}))-unmappedhost|(\d?[a-z]{2,4}(?:-[0-9][a-z]{2})?)-unmappedhost|(\w+)-idfc(\S+)?',i)

#([a-z]{3}-|(?=^[a-z]{6}-)([a-z]{6})|(?=^[a-z]{4}-)([a-z]{4})
     #print(next (it) )
     # for i in it:
     #     #print(f"Eye: {i}")
     #     print(f"Eye: {i.groups()}")

         # if i.group(2):
         #     print(f"Eye2: {i.groups()} and group:{i.group(2)}")


string = '''ABC1    1.1.1.1 20151119    active
            ABC2   2.2.2.2  20160000    inactive
            ABC3    x.x.x.x 20181111    active
'''

m = re.findall('(?=\w+\s+\S+\s+\d+\s+active)(\w+)',string)
#print(m)

rows = []
# with open("plainfile.txt","r") as f:
#     lines = f.readlines()
#     for line in lines:
#         rows.append(line.strip())
#         #count += 1
#         print("Line {}: {}".format('me', line.strip()))

#for i in rows:
   # print(f"I: {i}")

   