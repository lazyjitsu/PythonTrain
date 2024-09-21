import json

people_string = '''
{
    "people":[
        {
            "name":"Mikeo",
            "town":"Salas",
            "gang":"sem",
            "email":["mikeo@google.com","mike2@hotmail.com"]

        },
        {
            "name":"Richard",
            "town":"Salinas",
            "gang":"Freemont",
            "email":["mikeo@google.com","mike2@hotmail.com"]

        }
        
    ]
}
'''
data = json.loads(people_string)
for person in data['people']:
    print(person['name'],person['email'])
#print(data)
#new_json_string = json.dumps(data)
#new_json_string = json.dumps(data,indent=2)
new_json_string = json.dumps(data,indent=2,sort_keys=True)
print(f"json string: {new_json_string}")

with open('people.json') as f:
    data = json.load(f)

for person in data['people']:
    print(f"Person: {person} {person['email']} ")
    del person['email'][1]

with open('new_json_file','w') as f:
    json.dump(data,f,indent=2)

