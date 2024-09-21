import pandas as pd
raw_data = {'city': ['Salinas','San Jose','Gilroy','Prunedale','Chular','Morgan Hill'],
            'rank': ['1st','2nd','1st','2nd','1st','2nd'],
            'name': ['Marko','Karl','Jim','Joe','James','Tony'],
            'Score1':[44,48,39,41,38,44],
            'Score2':[68,88,92,38,55,33]}

#print(raw_data)

df = pd.DataFrame(raw_data, columns = ['city','rank','name','Score1','Score2'])

# print(df)
#d:\mySource\python>python MultiIndexDataFrames.py
#          city rank   name  Score1  Score2
#0      Salinas  1st  Marko      44      68
#1     San Jose  2nd   Karl      48      88
#2       Gilroy  1st    Jim      39      92
#3    Prunedale  2nd    Joe      41      38
#4       Chular  1st  James      38      55
#5  Morgan Hill  2nd   Tony      44      33

# drop=False means don't remove these columns, but do make them indicies (multidimensional)
df.set_index(['city','name'],drop=False,inplace=True)
print(df)
