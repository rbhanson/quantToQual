import pandas as pd

#Import the data from the sample csv.
df1 = pd.read_csv('Data.csv')

#Obtain the quartile break points and convert the pandas series into a dataframe.
dfq = pd.DataFrame(df1.Sample_Data.quantile([.2, .4, .6, .8]))

#Convert each qurtile break point into a variable.
quant1 = dfq.at[0.2,'Sample_Data']
quant2 = dfq.at[0.4,'Sample_Data']
quant3 = dfq.at[0.6,'Sample_Data']
quant4 = dfq.at[0.8,'Sample_Data']

#I like to print out the break points to check the results
print(quant1)
print(quant2)
print(quant3)
print(quant4)

#Create a new field named quartile and populate it with the logic.
df1['quantile'] = ['LL' if x< quant1 else 'LM' if quant1<=x<quant2 else 'M' if quant2<=x<quant3 else 'MH' if quant3<=x<quant4 else 'H' for x in df1['Sample_Data']]

#Save the dataframe to a new csv.
df1.to_csv('quantile.csv')
