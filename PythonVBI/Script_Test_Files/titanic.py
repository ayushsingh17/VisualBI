import pandas as pd 

df = pd.read_csv(r'C:\Users\hells\Downloads\PythonVBI\Script_Test_Files\titanic.csv')

print("\n",df.head(5),"\n")

df['Survived'] = df['Survived'].map({'Survived':1, 'Not Survived':0})
df['Sex'] = df['Sex'].map({'male':1, 'female':0})

df.to_csv(r'C:\Users\hells\Downloads\PythonVBI\Script_Test_Files\titanicNew.csv', index=False)