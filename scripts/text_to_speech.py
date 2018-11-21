from gtts import gTTS
import os
import pandas as pd


filename = input("Enter the filename: ")
df = pd.read_csv(filename, delimiter='\t', header=None, index_col=False)
df.reset_index(drop=True, inplace=True)

col = df.columns[0]
print(col)
# print(len(df.columns))

for _ in df.index.values:
    row = df.loc[_]
    df.at[_, col] = df.at[_, col][1:]
    print(df.at[_, col])

# print(df.columns)
df = df.to_string(index=False)

# print(df)

tts = gTTS(text=df, lang='en')

directory = filename[:-3]
tts.save(directory + 'mp3')

'''
/Users/jasonchang/Downloads/Lee_Performing_Asian_America_Critical_Strategies.txt
'''



