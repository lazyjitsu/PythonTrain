data = { "y2k" : [
                    {'WhlSale':
                        [
                            {'Policy1':
                                [
                                    {'Realm1':[                                        
                                        {'Desc':'mu Realm 1 and Policy 1 stuff',
                                        'Agents':['a1','a2'] 
                                        }       
    
                                            ]
                                    },
                                    {"Realm2": [
                                        {"Agents": ["r1","r2"],
                                        "Desc": "my cool realm 2 stuff"
                                        }
                                    ]
                            }
                        ]
                            },
                            {'Policy2':
                                [
                                    {'Realm1':[

                                        {'Desc':'my cool stuff for policy Two','Agents':
                                            ['p2r2-1','p2r2-2'] 
                                        }       
    
                                            ]
                                    }
                                ]
                            }
                        ]

                    }
                ]
}


for elArr in data['y2k']:
    for domain in elArr:
        print(f'Domain: {domain} ')
        for el in elArr[domain]:
            for policy in el:
                print(f"\tPolicy: {policy}")
                for realmElements in el[policy]:
                    for realmName in realmElements:
                        for el in realmElements[realmName]:
                            print(f"\t\tRealm: {realmName} amd {el['Desc']}")
                            for agents in el['Agents']:
                                print(f"\t\t\tAgents: {agents}")


#print(data)