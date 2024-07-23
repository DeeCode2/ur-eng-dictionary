import pandas as pd
#I've been using LibreOffice recently which saves the data in the .ods file format
#This is a simple function to convert it intto a csv file
df = pd.read_excel('urhobo-dictionary-table.ods')
df.to_csv('urhobo-dictionary.csv')
