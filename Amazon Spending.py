import pandas as pd 
import matplotlib as mp

df = pd.read_csv('Amazon-Orders.csv')
df = df.fillna(0)

startdate = pd.to_datetime(df['Order Date'].head(1))
enddate = pd.to_datetime(df['Order Date'].tail(1)) 

df['Total Charged'] = df['Total Charged'].str.replace('$', '').astype(float) 

total_spend = df['Total Charged'].sum()
mean_spend = df['Total Charged'].mean()
median_spend = df['Total Charged'].median() 
max_spend = df['Total Charged'].max() 
min_spend = df['Total Charged'].min()  

df['Tax Charged'] = df['Tax Charged'].str.replace('$', '').astype(float) 
total_tax = df['Tax Charged'].sum() 
mean_tax = df['Tax Charged'].mean() 
mean_tax_rate = mean_tax/mean_spend * 100

df['Order Date'] = pd.to_datetime(df['Order Date']) 
daily_orders = df.groupby('Order Date').sum()['Total Charged'] 
daily_orders.plot.bar(x = 'Order Date', y = "Total Charged", rot = 90, figsize=(20,10)) 

print("From ", startdate.to_string(index=False), "to ", enddate.to_string(index=False)) 
print("Your Total Spend on Amazon was $", round(total_spend,2)) 
print("Your Mean Spend on Amazon was $", round(mean_spend,2))
print("Your Max Spend on Amazon was $", round(max_spend,2)) 

print("The Mean Sales Tax was", round(mean_tax_rate,2), "%") 

mp.pyplot.show() 




