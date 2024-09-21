a = ["side walk breakers","marko","christina","jam city crew"]
b = []
c = int(0)
for i in a:
    b.append({i:len(i)})
    if len(i) > 10:
        
        #print(f"I: {b[c]}")
        c += 1
for i in range(len(b)):
    #b[i]['Size'] = len(b[i][a[i]])
    print(f"Data: {b[i]} Key:{a[i]} and J: {b[i][a[i]]}")

print("-------------------------------")
for i in b:
    #i['Size'] = len(b[i])
    print(i)