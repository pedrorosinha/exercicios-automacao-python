import pandas as pd



df = pd.read_excel('data/input/supermarket_sales.xlsx')

df = df[['Gender', 'Product line', 'Total']]

pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)

pivot_table.to_excel('data/output/pivot_table.xlsx', sheet_name='Report', startrow=4)