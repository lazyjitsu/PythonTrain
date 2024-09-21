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


jdata = {}
jdata = { "y2k" : [
                    {'WhlSale':
                        [
                            {'Policy1':
                                [
                                    {'Realm1':[                                        
                                        {'Desc':'my cool stuff',
                                        'Agents':['a1','a2'] 
                                        }       
    
                                            ]
                                    },
                                    {"Realm2": [
                                        {"Agents": ["a1","a2"],
                                        "Desc": "my cool stuff"
                                        }
                                    ]
                            }
                        ]
                            },
                            {'Policy2':
                                [
                                    {'Realm1':[

                                        {'Desc':'my cool stuff','Agents':
                                            ['a1','a2'] 
                                        }       
    
                                            ]
                                    }
                                ]
                            }
                        ]

                    }
                ]
}

#print(data)
#new_json_string = json.dumps(data)
#new_json_string = json.dumps(data,indent=2)
new_json_string = json.dumps(jdata,indent=3,sort_keys=True)
print(f"json string: {new_json_string}")

bankdata = json.loads(new_json_string)


with open('bankOnJson','w') as f:
    json.dump(bankdata,f,indent=3)